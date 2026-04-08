import mysql.connector
import json

def connector_db():
    with open("config.json") as  f:
        config = json.load(f)
    
    return mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"]
    )   