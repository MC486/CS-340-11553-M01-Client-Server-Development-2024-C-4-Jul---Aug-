from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initialize the MongoClient
        self.client = MongoClient(f'mongodb://{username}:{password}@nv-desktop-services.apporto.com:31790/AAC?authSource=admin')
        self.database = self.client['AAC']
        self.collection = self.database['animals']

    def create (self, data):
        """ Method to insert a document into the animals collection """
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"An error occured: {e}")
                return False
            else:
                raise ValueError("Data parameter is empty")

    def read(self, query):
        """ Method to query documents from the animals collection """
        if query is not None:
            try:
                return list(self.collection.find(query))
            except Exception as e:
                print(f"An error occured: {e}")
                return []
            else:
                raise ValueError("Query parameter is empty")

    def update(self, query, new_values):
        """ Method to update documents in the animals collection """
        if query is not None and new_values is not None:
            try:
                result = self.collection.update_many(query, {'$set': new_values})
                return result.modified_count
            except Exception as e:
                print(f"An error occurred: {e}")
                return 0
        else:
            raise ValueError("Query or new_values parameter is empty")
            
    def delete(self, query):
        """ Method to delete documents from the animals collection """
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print(f"An error occurred: {e}")
                return 0
        else:
            raise ValueError("Query parameter is empty")