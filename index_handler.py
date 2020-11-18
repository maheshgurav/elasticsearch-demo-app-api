# Index handling script

import argparse
from argparse import RawTextHelpFormatter
from logger_config import get_logger
from elasticsearch import Elasticsearch
import requests
import json

logger = get_logger(__name__)


def create_index(index_name):
    # create a new instance of the Elasticsearch client class
    response = None
    try:
        logger.debug("Getting elastic search object")
        elastic_search = Elasticsearch()
        if not elastic_search.indices.exists(index_name):
            logger.debug("Creating index {}".format(index_name))
            response = elastic_search.indices.create(index=index_name)
            logger.debug("Index '{}' created successfully".format(index_name))
        else:
            logger.debug("Index '{}' is already exists".format(index_name))
    except Exception as ex:
        logger.error(ex)


def reindex(source_index, destination_index):
    try:
        reindex_data = {}
        reindex_data["source"] = {"index" : source_index}
        reindex_data["dest"] = {"index" : destination_index}
        response = requests.post("http://localhost:9200/_reindex", data = json.dumps(reindex_data), headers={"Content-Type" : "application/json"})
    except Exception as ex:
        logger.error(ex)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=RawTextHelpFormatter, description='Create Indexes...')
    parser.add_argument('-o', '--operation',
                        type=str, help='Operations can be either of "create" or "reindex"')    
    parser.add_argument('-n', '--index_name',
                        type=str, help='Index name...')
    parser.add_argument('-s', '--source_index',
                        type=str, help='Source index name...')
    parser.add_argument('-d', '--destination_index',
                        type=str, help='Destination index name...')
    args = parser.parse_args()
    if args.operation == "create":
        create_index(args.index_name)
    if args.operation == "reindex":
        reindex(args.source_index, args.destination_index)
