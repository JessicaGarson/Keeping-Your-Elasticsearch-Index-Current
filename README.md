# Keeping Your Elasticsearch Index Current with Python and Google Cloud Platform Functions

This repository contains a Python script designed for automatically updating an Elasticsearch index to ensure the data remains current, especially useful for applications with dynamic data. The script is deployable via Google Cloud Platform (GCP), utilizing Cloud Functions for execution and Cloud Scheduler for periodic updates. 

## Resources
* Blog post on [Keeping Your Elasticsearch Index Current with Python and Google Cloud Platform Functions](https://www.elastic.co/search-labs/blog/articles/keeping-your-elasticsearch-index-current-with-python-and-google-cloud-platform-functions)
* [Jupyter Notebook](https://github.com/elastic/elasticsearch-labs/blob/main/supporting-blog-content/keeping-your-index-current/local_testing.ipynb) for local testing.


## Prerequisites

* This example uses Elasticsearch version 8.12; if you are new, check out our Quick Start on [Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html).
* Download the latest version of Python if you don't have it installed on your machine. This example utilizes Python 3.12.1.
* [An API key](https://api.nasa.gov/) for NASA's APIs.

## Getting help

Let us know if you need if this blog post inspires you to build anything or if you have any questions on our [Discuss forums](https://discuss.elastic.co/) and [the community Slack channel](https://communityinviter.com/apps/elasticstack/elastic-community).
