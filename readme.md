## AIRFLOW NEO4J BioXML Process

This project is an example of how to process a complex XML and load it into a NEO4J database graph with an AIRFLOW orchestration.

## Run in local

# Preconditions
To run this locally we are going to need to have AIRFLOW and NEO4j installed.
For references on this see the following links:

```bash
NEO4J --> https://neo4j.com/docs/operations-manual/current/
```

```bash
AIRFLOW -->  https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html
```
This version is not yet dockerized

# File structure
Inside the AIRFLOW folder, we find a dags/src folder where the data, functions and configuration access files are, which will be used in common by the different Dags (for now there is only one first dag)
The XML paring is designed ad hoc for the XML with biological data found in the dags/data folder.

## files in src folder

In functions.py we find the functions used to search and save the records in the NEO4J database.

In the file accessdata.py we have all the db queries

In the config.py file, the credentials to connect to the DB are configured (this must be varied with the data of the NEO4J database that you want to use). In a productive version, this would be replaced by environment variables.

## First DAG

In the dags folder the first DAG contains the necessary login for the XML traversal, the Protein, Organism, Gene, FullName, Feature, Reference and Author nodes were taken into account to load the DB in the DB. (In all cases this title was put as tag:name and a tag:real_name was included to load the name of the node when it had it.)

There are other nodes in the XML like evidence, dbReference, proteinExistence and some more, as well as other attributes and values that are not included in this version.
A graph of 221 nodes and their relationships is generated, understanding that the point of the exercise is clear and it is not necessary to include each node that is not going to add new difficulty and takes time.

