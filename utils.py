import toml

from pymongo import MongoClient

def connect_to_collection(database_name, collection_name):
    # Establish a connection to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    # Access the specified database
    database = client[database_name]
    # Return the desired collection
    return database[collection_name]

def read_toml(file_path):
    with open(file_path, "r") as f:
        return toml.load(f)