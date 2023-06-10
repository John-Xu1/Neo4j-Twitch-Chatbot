import neo4j
from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

load_dotenv()
hostName = os.environ.get('NEO4J_URI')
user = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
graphDBDriver = GraphDatabase.driver(uri=hostName, auth=(user, password))


def runQuery(q, p):
    with graphDBDriver.session() as session:
        result = session.run(query=q, parameters=p)
        data = []
        for record in result:
            data.append(record.values()[0])
        return data
