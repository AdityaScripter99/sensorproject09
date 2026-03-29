from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#URL
uri = "mongodb+srv://aditya:bxspv9wISMv2zkV1@cluster0.ziyrllc.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Create Database name and Collection Name 
DATABASE_NAME = "aditech"
COLLECTION_NAME = "waferfault" 

df = pd.read_csv("/home/aditya/SENSOR_PROJECT/notebooks/wafer.csv")

df = df.drop("Unnamed: 0",axis = 1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)