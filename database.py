import pymongo
import constants as c


class MongoDB:
    def __init__(self, connection_string, database, collection):
        self.client = pymongo.MongoClient(connection_string)
        self.db = self.client[database]
        self.collection = self.db[collection]
        
    def get_collection_size(self):
        return self.db.command('collstats', c.MONGO_DB_COLLECTION)['count']
        
    def get_last_document(self):
        return self.collection.find().sort("id", -1)[0]
        
    def insert_one_document(self, _dict):
        return self.collection.insert_one(_dict)
    
    def generate_id(self):
        collection_size = self.get_collection_size()
        if collection_size == c.EMPTY:
            return c.INITIAL_ID
        else: 
            return collection_size + 1
