# Keeping Your Elasticsearch Index Current with Python and Google Cloud Platform Functions

This repository contains a Python script designed for automatically updating an Elasticsearch index to ensure the data remains current, especially useful for applications with dynamic data. The script is deployable via Google Cloud Platform (GCP), utilizing Cloud Functions for execution and Cloud Scheduler for periodic updates. 


## Prerequisites

* This example uses Elasticsearch version 8.12; if you are new, check out our Quick Start on [Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html).
* Download the latest version of Python if you don't have it installed on your machine. This example utilizes Python 3.12.1.
* [An API key](https://api.nasa.gov/) for NASA's APIs.
* You will use the [Requests](https://requests.readthedocs.io/en/latest/) package to connect to a NASA API, [Pandas](https://pandas.pydata.org/) to manipulate data, the [Elasticsearch Python Client](https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/getting-started-python.html) to load data into an index and keep it up to date, and [Jupyter Notebooks](https://docs.jupyter.org/en/latest/) to work with your data interactively while testing. You can run the following line to install these required packages:

    ```
    pip3 install requests pandas elasticsearch notebook
    ```
