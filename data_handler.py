# Script for data injestion

import argparse
from argparse import RawTextHelpFormatter
from logger_config import get_logger
from elasticsearch import Elasticsearch, helpers
import csv

import json
import requests
from datetime import datetime

logger = get_logger(__name__)


def load_data(input_file, index_name):
    try:
        elastic_search = Elasticsearch()
        with open(input_file) as f:
            reader = csv.DictReader(f)
            rows = []
            for row in reader:
                row["_index"] = index_name
                rows.append(row)
            helpers.bulk(elastic_search, rows)
    except Exception as ex:
        logger.error(ex)


def update_data(index_name):
    try:
        body = {}
        body["query"] = {"match_all": {}}
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        new_field_details = "ctx._source.last_updated = \"{}\";".format(date_time) 
        body["script"] = {"inline": new_field_details} 
        url = "http://localhost:9200/{}/_update_by_query".format(index_name)
        response = requests.post(url, data = json.dumps(body), headers={"Content-Type" : "application/json"})
        if response.status_code == 200:
            logger.debug("Added new field to documents")
    except Exception as ex:
        logger.error(ex)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=RawTextHelpFormatter, description='Data handler...')
    parser.add_argument('-o', '--operation',
                    type=str, help='Operations can be either of "upload" or "update"')
    parser.add_argument('-file', '--input_file',
                        type=str, help='Input file path...')
    parser.add_argument('-index', '--index_name',
                        type=str, help='Index name...')    
    args = parser.parse_args()
    if args.operation == "upload":
        load_data(args.input_file, args.index_name)
    if args.operation == "update":
        update_data("project_*")
