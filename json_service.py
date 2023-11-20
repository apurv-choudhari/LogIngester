from typing import Collection
from pymongo import MongoClient
from flask import Flask, request, jsonify
import os
import threading
import certifi

def connect_to_mongodb(connection_string):
    uri = f"{connection_string}"
    client = MongoClient(uri, tlsCAFile=certifi.where())
    database_name = "MyDB"
    try:
        dbs = client.list_database_names()
        print(dbs)
        client[database_name].list_collection_names()
        db = client[database_name]
        return db
    except Exception as e:
        raise ConnectionError(f"Unable to connect to MongoDB: {e}")

app = Flask(__name__)
db = None

@app.route('/json', methods=['POST'])
def json_route():
    data = request.json
    handle_request(data)
    return jsonify({"status": "success"})

def handle_request(data):
    print(data)
    collection = db.injester
    collection.insert_one(data)
    pass

if __name__ == '__main__':
    try:
        connection_string = os.getenv("MONGO_CONNECTION_STRING")
        db = connect_to_mongodb(connection_string)

        server_thread = threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 3000, 'threaded': True})
        server_thread.start()
        server_thread.join()

    except Exception as e:
        print(f"Exception: {e}")
