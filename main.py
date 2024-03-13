import functions_framework
import requests
import os
import pandas as pd
from datetime import datetime
from elasticsearch import Elasticsearch, helpers


def connect_to_elastic():
    elastic_cloud_id = os.getenv("ELASTIC_CLOUD_ID")
    elastic_api_key = os.getenv("ELASTIC_API_KEY")
    return Elasticsearch(cloud_id=elastic_cloud_id, api_key=elastic_api_key)


def connect_to_nasa(last_update_date):
    url = "https://api.nasa.gov/neo/rest/v1/feed"
    nasa_api_key = os.getenv("NASA_API_KEY")
    params = {
        "api_key": nasa_api_key,
        "start_date": last_update_date,
        "end_date": datetime.now(),
    }
    return requests.get(url, params).json()


def create_df(response):
    all_objects = []
    for date, objects in response["near_earth_objects"].items():
        for obj in objects:
            obj["close_approach_date"] = date
            all_objects.append(obj)
    df = pd.json_normalize(all_objects)
    return df.drop("close_approach_data", axis=1)


def doc_generator(df, index_name):
    for index, document in df.iterrows():
        yield {
            "_index": index_name,
            "_id": f"{document['close_approach_date']}",
            "_source": document.to_dict(),
        }


def updated_last(es, index_name):
    query = {
        "size": 0,
        "aggs": {"last_date": {"max": {"field": "close_approach_date"}}},
    }
    response = es.search(index=index_name, body=query)
    last_updated_date_string = response["aggregations"]["last_date"]["value_as_string"]
    datetime_obj = datetime.strptime(last_updated_date_string, "%Y-%m-%dT%H:%M:%S.%fZ")
    return datetime_obj.strftime("%Y-%m-%d")


def update_new_data(df, es, last_update_date, index_name):
    if isinstance(last_update_date, str):
        last_update_date = datetime.strptime(last_update_date, "%Y-%m-%d")

    last_update_date = pd.Timestamp(last_update_date).normalize()

    if not df.empty and "close_approach_date" in df.columns:
        df["close_approach_date"] = pd.to_datetime(df["close_approach_date"])

    today = pd.Timestamp(datetime.now().date()).normalize()

    if df is not None and not df.empty:
        update_range = df.loc[
            (df["close_approach_date"] > last_update_date)
            & (df["close_approach_date"] < today)
        ]
        print(update_range)
        if not update_range.empty:
            helpers.bulk(es, doc_generator(update_range, index_name))
        else:
            print("No new data to update.")
    else:
        print("The DataFrame is empty or None.")


# Triggered from a message on a Cloud Pub/Sub topic.
@functions_framework.cloud_event
def hello_pubsub(cloud_event):
    index_name = "asteroids_data"
    es = connect_to_elastic()
    last_update_date = updated_last(es, index_name)
    print(last_update_date)
    response = connect_to_nasa(last_update_date)
    df = create_df(response)
    try:
        if df is None:
            raise ValueError("DataFrame is None. There may be a problem.")
        update_new_data(df, es, last_update_date, index_name)
        print(updated_last(es, index_name))
    except Exception as e:
        print(f"An error occurred: {e}")
