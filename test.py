import unittest
import json

from app import app
from pymongo import MongoClient
from pymongo.collection import Collection
from utils import connect_to_collection

class TestBookstoreInventory(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.item = {
            "title": "The Catcher in the Rye",
            "author": "J.D. Salinger",
            "genre": "Fiction"
        }
    
    def test_connect_to_collection(self):
        # Specify the test database and collection names
        test_database_name = 'test'
        test_collection_name = 'testCollection'

        # Connect to the test collection
        collection = connect_to_collection(test_database_name, test_collection_name)

        # Verify that the connection is successful
        self.assertIsInstance(collection, Collection)
        self.assertEqual(collection.database.name, test_database_name)
        self.assertEqual(collection.name, test_collection_name)

    def test_homepage(self):
        response = self.app.get('/')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Hello, this is the homepage of the bookstore inventory management system!')

    def test_get_all_items(self):
        response = self.app.get('/items')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(data, list))

    def test_get_one_item(self):
        item_id = '645f97afb36ba179ff2f5f91'  # Replace with an existing item id
        response = self.app.get(f'/items/{item_id}')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['_id'], item_id)

    def test_add_item(self):
        response = self.app.post('/add', data=json.dumps(self.item), content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 201)
        self.assertTrue(isinstance(data['_id'], str))

    def test_update_item(self):
        item_id = '6460beb944f39022373398f6'  # Replace with an existing item id
        updated_item = {
            "genre": "Fantasy"
        }
        response = self.app.put(f'/items/update/{item_id}', data=json.dumps(updated_item), content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Item updated successfully')

    def test_delete_item(self):
        item_id = '6460dd1a1957bb137aae2e55'  # Replace with an existing item id
        response = self.app.delete(f'/items/delete/{item_id}')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Item deleted successfully')

if __name__ == '__main__':
    unittest.main()