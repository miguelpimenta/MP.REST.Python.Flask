from pymongo import MongoClient
from bson.objectid import ObjectId
from app.config.config import mongoConn as m

def get_dal():
    return DAL(m['username'], m['password'], m['host'], m['port'], m['db_name'])

class DAL:

    def __init__(self, username, password, host, port, db_name):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.db_name = db_name
        self.uri = self.create_connection_uri()
        self.client = MongoClient(self.uri)

    # Create Connection string
    def create_connection_uri(self):
        return 'mongodb://' + self.username + ':' + self.password + '@' + self.host + ':' + self.port + '/' + self.db_name

    # Crete / Insert
    def create(self, collection_name, item):
        db = self.client[self.db_name]
        collection = db[collection_name]
        return collection.insert_one(item).inserted_id

    # Find
    def find(self, collection_name, column_name, search_terms):
        db = self.client[self.db_name]
        collection = db[collection_name]
        return collection.find({column_name: search_terms})

    # List All
    def get(self, collection_name):
        out = []
        db = self.client[self.db_name]
        collection = db[collection_name]
        items = collection.find()
        for item in items:
            out.append(item)
        return out

    # Get One
    def get_by_id(self, collection_name, item_id):
        db = self.client[self.db_name]
        collection = db[collection_name]
        return collection.find_one({'_id': ObjectId(item_id)})

    # Update
    def update(self, collection_name, item_id, item):
        db = self.client[self.db_name]
        collection = db[collection_name]
        return collection.update({'_id': ObjectId(item_id)}, item, upsert=False)

    # Replace
    def replace(self, collection_name, item_id, item):
        db = self.client[self.db_name]
        collection = db[collection_name]
        return collection.replace_one({'_id': ObjectId(item_id)}, item, upsert=False)

    # Delete
    def delete(self, collection_name, item_id):
        db = self.client[self.db_name]
        collection = db[collection_name]
        return collection.remove({'_id': ObjectId(item_id)})

    """ System """
    # Create Collection
    def create_collection(self, collection_name):
        db = self.client[self.db_name]
        db.create_collection(collection_name)

    # Drop Collection
    def drop_collection(self, collection_name):
        db = self.client[self.db_name]
        db.drop_collection(collection_name)