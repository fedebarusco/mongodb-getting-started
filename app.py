import logging
import json

from flask import Flask, jsonify, request
from utils import read_toml, connect_to_collection
from pymongo import MongoClient
from bson import ObjectId, json_util

# Create the Flask application, set logging level and load configuration
app = Flask(__name__)
app.logger.setLevel(logging.INFO)
conf = read_toml('config.toml')
app.config.from_object(conf)

# Establish a connection to MongoDB
collection = connect_to_collection(conf['DATABASE_NAME'], conf['COLLECTION_NAME'])

# Define a route for the homepage
@app.route("/")
def hello():
    return jsonify({'message': 'Hello, this is the homepage of the bookstore inventory management system!'})

# Define a route to get all items of the collection
@app.route("/items", methods=['GET'])
def get_items():
    # Retrieve all items from the collection
    items  = list(collection.find())
    # Serialize items to JSON using the json_util module
    json_items = json.dumps(items, default=json_util.default, indent=2)
    # Return the JSON response with proper headers
    response = app.response_class(
        response=json_items,
        status=200,
        mimetype='application/json'
    )
    return response

# Define a route to get one item of the collection by id
@app.route("/items/<item_id>", methods=['GET'])
def get_item(item_id):
    # Convert the item_id parameter to ObjectId
    item_id = ObjectId(item_id)
    # Check if the item exists in the collection
    item = collection.find_one({'_id': item_id})
    if item:
         # Convert the ObjectId to a string
        item['_id'] = str(item['_id'])
        # Serialize items to JSON using the json_util module
        json_item = json.dumps(item, default=json_util.default, indent=2)
        # Return the JSON response with proper headers
        response = app.response_class(
            response=json_item,
            status=200,
            mimetype='application/json'
        )
        return response
    else:
        return jsonify({'message': 'Item not found'})

# Define a route to add one item to the collection
@app.route('/items', methods=['POST'])
def add_item():
    # Get the data from the request
    data = request.get_json()
    # Insert the item into the collection
    item_id = collection.insert_one(data).inserted_id
    # Return the ID of the inserted item
    return jsonify({'_id': str(item_id)}), 201

# Define a route to update one item of the collection by id
@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    # Convert the item_id parameter to ObjectId
    item_id = ObjectId(item_id)
    # Check if the item exists in the collection
    existing_item = collection.find_one({'_id': item_id})
    if existing_item:
        # Update the item with the new one
        updated_item = request.get_json()
        collection.update_one({'_id': item_id}, {'$set': updated_item})
        return jsonify({'message': 'Item updated successfully'})
    else:
        return jsonify({'message': 'Item not found'})

# Define a route to delete one item from the collection by id
@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    # Convert the item_id parameter to ObjectId
    item_id = ObjectId(item_id)
    # Check if the item exists in the collection
    item = collection.find_one({'_id': item_id})
    if item:
        # Delete the item from the collection
        collection.delete_one({'_id': item_id})
        return jsonify({'message': 'Item deleted successfully'})
    else:
        return jsonify({'message': 'Item not found'})

# Run the application
if __name__ == '__main__':
    app.run(debug=True)