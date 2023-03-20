from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import logging

from src.config import config
from src.functions import AppNeo4jTransactions
import xml.etree.ElementTree as ET

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['adriantintpilver@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

def Load_and_process_XML():
    logging.info("performing load and process XML")
    #set te xmlns value
    ns="{http://uniprot.org/uniprot}"
    #open ne4j conexion
    app = AppNeo4jTransactions(config['NEO4J_URL'], config['NEO4J_USER'], config['NEO4J_PASSWORD'])
    #open the xml file
    tree = ET.parse("airflow\dags\data\Q9Y261.xml")
    root = tree.getroot()
    for child in root:
        if child.tag == ns+"entry":
            proteinID = str(child.find(ns+'accession').text)
            for child2 in child:
                # proteins
                if str(child2.tag) == ns+"protein":
                    app.create_relationship("HAS_FULL_NAME", "", "", "Protein", "FullName","", str(child2.find(ns+'recommendedName//'+ns+'fullName').text), proteinID, "", "", "", "", "")
                # gene
                if str(child2.tag) == ns+"gene":
                    for child3 in child2:
                        app.create_relationship("FROM_GENE", "", child3.attrib['type'], "Protein", "Gene", "", str(child3.text), proteinID, "", "", "", "", "")
                # organism 
                if str(child2.tag) == ns+"organism":
                    app.create_relationship("IN_ORGANISM", "", "", "Protein", "Organism", "", str(child2.find(ns+'name').text), proteinID, "", "", "", "", str(child2.find(ns+'dbReference').attrib['id']))
                # feature
                if str(child2.tag) == ns+"feature":
                    if 'description' in child2.attrib and 'type' in child2.attrib:
                        position = ""
                        for child3 in child2.find(ns+'location'):
                            if child3.tag == ns+'position':
                                position = str(child3.attrib['position'])
                            if child3.tag == ns+'begin':
                                position = str(child3.attrib['position'])
                            if child3.tag == ns+'end':
                                position = position + " - " + str(child3.attrib['position'])
                        app.create_relationship("HAS_FEATURE", position, "", "Protein", "Feature", "", child2.attrib['description'], proteinID, "", "", child2.attrib['type'], "", "")    
                #reference
                if str(child2.tag) == ns+"reference":
                    if 'name' in child2.find(ns+'citation').attrib:
                        name = child2.find(ns+'citation').attrib['name']
                    else:
                        name = ""
                    if 'volume' in child2.find(ns+'citation').attrib:
                        volume = child2.find(ns+'citation').attrib['volume']
                    else:
                        volume = ""
                    if 'first' in child2.find(ns+'citation').attrib:
                        first = child2.find(ns+'citation').attrib['first']
                    else:
                        first = ""
                    if 'last' in child2.find(ns+'citation').attrib:
                        last = child2.find(ns+'citation').attrib['last']
                    else:
                        last = ""
                    app.create_relationship_reference("HAS_REFERENCE", "", "", "Protein", "Reference", "", name, proteinID, child2.attrib['key'], "", child2.find(ns+'citation').attrib['type'], "", child2.find(ns+'citation').find(ns+'title').text, child2.find(ns+'scope').text, child2.find(ns+'citation').attrib['date'], volume, first, last)    
                    #author
                    for child3 in child2.find(ns+'citation').find(ns+'authorList'):
                        app.create_relationship_reference("HAS_AUTHOR", "", "", "Author", "Reference", child3.attrib['name'], name, "", child2.attrib['key'], "", child2.find(ns+'citation').attrib['type'], "", child2.find(ns+'citation').find(ns+'title').text, child2.find(ns+'scope').text, child2.find(ns+'citation').attrib['date'], volume, first, last)    

def end():
    logging.info("performing end")


with DAG(
    'first',
    default_args=default_args,
    description='First DAG',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=['Load and process XML', 'End'],
) as dag:
    Load_and_process_XML_task = PythonOperator(task_id='Load_and_process_XML', python_callable=Load_and_process_XML)
    end_task = PythonOperator(task_id='end', python_callable=end)

    Load_and_process_XML_task >> end_task

if __name__ == "__main__":
    Load_and_process_XML()
