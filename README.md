### Pre-requisites

Please make sure that your installation server has following softwares/packages installed 
1. [Python-3.x](https://www.python.org/downloads/)
1. [Virtualenv](https://virtualenv.pypa.io/en/stable/)
1. [Java](https://docs.datastax.com/en/jdk-install/doc/jdk-install/installOracleJdkDeb.htm)

### Installation

1. To install elasticsearch, run the following command
	```
	sh install_elasticsearch.sh
	```
1. Install python libraries from pip
	```
	pip install -r requirements.txt
	```

### Scripts

#### Index creation script

To create index please use following script,
```
index_handler.py -o create -n <INDEX NAME> 
```

#### Re-indexing script

To re-index please use following script,
```
index_handler.py -o reindex -s <SOURCE INDEX NAME> -d <DESTINATION INDEX NAME>
```


#### Add new field to indexex matching project_*

To re-index please use following script,
```
data_handler.py -o update
```
