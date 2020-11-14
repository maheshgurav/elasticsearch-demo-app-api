# Index handling script

import argparse
from argparse import RawTextHelpFormatter
from logger_config import get_logger
from elasticsearch import Elasticsearch

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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=RawTextHelpFormatter, description='Create Indexes...')
    parser.add_argument('-name', '--index_name',
                        type=str, help='Index name...')
    args = parser.parse_args()
    create_index(args.index_name)
