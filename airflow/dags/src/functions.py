from neo4j import GraphDatabase
import logging
from neo4j.exceptions import ServiceUnavailable
from flask import Flask
from datetime import datetime

from src.accessdata import neo4j_querys
from src.config import config


now = datetime.now()
app = Flask(__name__)

class AppNeo4jTransactions:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_relationship(self, relationtag, postition, status, node1_name, node2_name, node1_real_name, node2_real_name, node1_id, node2_id, node1_type, node2_type, node1_taxonomy_id, node2_taxonomy_id):
        with self.driver.session(database="neo4j") as session:
            result = session.execute_write(
                self._create_and_return_relationship, relationtag, postition, status, node1_name, node2_name, node1_real_name, node2_real_name, node1_id, node2_id, node1_type, node2_type, node1_taxonomy_id, node2_taxonomy_id)
            for row in result:
                print("Created relationship between: {n1}, {n2}".format(n1=row['n1'], n2=row['n2']))

    @staticmethod
    def _create_and_return_relationship(tx, relationtag, postition, status, node1_name, node2_name, node1_real_name, node2_real_name, node1_id, node2_id, node1_type, node2_type, node1_taxonomy_id, node2_taxonomy_id):
        query = neo4j_querys['query_if_not_exist_create_and_return_relationship'].replace('$relationtag', relationtag).replace('$postition', postition).replace('$status', status)
        result = tx.run(query, relationtag=relationtag, postition=postition, status=status, node1_name=node1_name, node2_name=node2_name, node1_real_name=node1_real_name, node2_real_name=node2_real_name, node1_id=node1_id, node2_id=node2_id, node1_type=node1_type, node2_type=node2_type, node1_taxonomy_id=node1_taxonomy_id, node2_taxonomy_id=node2_taxonomy_id)
        try:
            return [{"n1": row["n1"]["name"], "n2": row["n2"]["name"]}
                    for row in result]
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=neo4j_querys['query_create_and_return_relationship'], exception=exception))
            raise
    def create_relationship_reference(self, relationtag, postition, status, node1_name, node2_name, node1_real_name, node2_real_name, node1_id, node2_id, node1_type, node2_type, node1_taxonomy_id, title, scope, date, volume, first, last):
        with self.driver.session(database="neo4j") as session:
            result = session.execute_write(
                self._create_and_return_relationship_reference, relationtag, postition, status, node1_name, node2_name, node1_real_name, node2_real_name, node1_id, node2_id, node1_type, node2_type, node1_taxonomy_id, title, scope, date, volume, first, last)
            for row in result:
                print("Created relationship between: {n1}, {n2}".format(n1=row['n1'], n2=row['n2']))

    @staticmethod
    def _create_and_return_relationship_reference(tx, relationtag, postition, status, node1_name, node2_name, node1_real_name, node2_real_name, node1_id, node2_id, node1_type, node2_type, node1_taxonomy_id, title, scope, date, volume, first, last):
        query = neo4j_querys['query_if_not_exist_create_and_return_relationship_reference'].replace('$relationtag', relationtag).replace('$postition', postition).replace('$status', status)
        result = tx.run(query, relationtag=relationtag, postition=postition, status=status, node1_name=node1_name, node2_name=node2_name, node1_real_name=node1_real_name, node2_real_name=node2_real_name, node1_id=node1_id, node2_id=node2_id, node1_type=node1_type, node2_type=node2_type, node1_taxonomy_id=node1_taxonomy_id, title=title, scope=scope, date=date, volume=volume, first=first, last=last)
        try:
            return [{"n1": row["n1"]["name"], "n2": row["n2"]["name"]}
                    for row in result]
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=neo4j_querys['query_create_and_return_relationship'], exception=exception))
            raise
    def create_relationship_reference_author(self, relationtag, postition, status, node1_name, node2_name, node1_real_name, node2_real_name, node1_id, node2_id, node1_type, node2_type, node1_taxonomy_id, title, scope, date, volume, first, last):
        with self.driver.session(database="neo4j") as session:
            result = session.execute_write(
                self._create_and_return_relationship_reference_author, relationtag, postition, status, node1_name, node2_name, node1_real_name, node2_real_name, node1_id, node2_id, node1_type, node2_type, node1_taxonomy_id, title, scope, date, volume, first, last)
            for row in result:
                print("Created relationship between: {n1}, {n2}".format(n1=row['n1'], n2=row['n2']))

    @staticmethod
    def _create_and_return_relationship_reference_author(tx, relationtag, postition, status, node1_name, node2_name, node1_real_name, node2_real_name, node1_id, node2_id, node1_type, node2_type, node1_taxonomy_id, title, scope, date, volume, first, last):
        query = neo4j_querys['query_if_not_exist_create_and_return_relationship_reference_author'].replace('$relationtag', relationtag).replace('$postition', postition).replace('$status', status)
        result = tx.run(query, relationtag=relationtag, postition=postition, status=status, node1_name=node1_name, node2_name=node2_name, node1_real_name=node1_real_name, node2_real_name=node2_real_name, node1_id=node1_id, node2_id=node2_id, node1_type=node1_type, node2_type=node2_type, node1_taxonomy_id=node1_taxonomy_id, title=title, scope=scope, date=date, volume=volume, first=first, last=last)
        try:
            return [{"n1": row["n1"]["name"], "n2": row["n2"]["name"]}
                    for row in result]
        # Capture any errors along with the query and data for traceability
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=neo4j_querys['query_create_and_return_relationship'], exception=exception))
            raise
    def find_node(self, node_name, node_id, node_type, node_taxonomy_id):
        with self.driver.session(database="neo4j") as session:
            result = session.execute_read(self._find_and_return_node, node_name, node_id, node_type, node_taxonomy_id)
            for row in result:
                print("Found node: {row}".format(row=row))
                return [row]

    @staticmethod
    def _find_and_return_node(tx, node_name, node_id, node_taxonomy_id, node_type):
        result = tx.run(neo4j_querys['query_find_and_return_node'], node_name=node_name, node_id=node_id, node_type=node_type, node_taxonomy_id=node_taxonomy_id)
        return [row["ID"] for row in result]
 
