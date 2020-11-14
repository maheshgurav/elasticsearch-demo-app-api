# Script for data injestion

import argparse
from argparse import RawTextHelpFormatter
from logger_config import get_logger
from elasticsearch import Elasticsearch, helpers
import csv

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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=RawTextHelpFormatter, description='Create Indexes...')
    parser.add_argument('-file', '--input_file',
                        type=str, help='Input file path...')
    parser.add_argument('-index', '--index_name',
                        type=str, help='Index name...')
    args = parser.parse_args()
    load_data(args.input_file, args.index_name)
