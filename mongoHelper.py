import json
import pymongo
from bson import json_util


class MongoHelper:
    # def __init__(self):
    #     pass

    def __init__(self, mongodb_host, mongodb_port, db_name, collection_name):
        self.MONGODB_HOST = mongodb_host
        self.MONGODB_PORT = mongodb_port
        self.DB_NAME = db_name
        self.COLLECTION_NAME = collection_name
        self.documents = None

        self.mongo_connect(self.MONGODB_HOST, self.MONGODB_PORT, self.DB_NAME, self.COLLECTION_NAME)

    def mongo_connect(self, mongodb_host, mongodb_port, db_name, collection_name):
        self.MONGODB_HOST = mongodb_host
        self.MONGODB_PORT = mongodb_port
        self.DB_NAME = db_name
        self.COLLECTION_NAME = collection_name
        connection = pymongo.MongoClient(self.MONGODB_HOST, self.MONGODB_PORT)
        # connection = pymongo.MongoClient("mongodb://localhost:27017/")
        self.documents = connection[self.DB_NAME][self.COLLECTION_NAME]
        # return self.documents

    # def mongo_connect(self):
    #     connection = pymongo.MongoClient(self.MONGODB_HOST, self.MONGODB_PORT)
    #     # connection = pymongo.MongoClient("mongodb://localhost:27017/")
    #     self.documents = connection[self.DB_NAME][self.COLLECTION_NAME]
    #     # return self.documents

    # def connection_close(self):
    #     self.documents.close()

    def find(self, query):
        results = self.documents.find(query)
        return results

    def insert_one_data(self, data):
        try:
            self.documents.insert_one(data)
        except:
            print("insert failed")
        else:
            print("insert successed")

    def insert_many_data(self, data_list):
        try:
            self.documents.insert_many(data_list)
        except:
            print("insert failed")
        else:
            print("insert successed")

    def delete_one_data(self, query):
        try:
            self.documents.delete_one(query)
        except:
            print("delete failed")
        else:
            print("delete successed")

    def delete_many_data(self, query):
        try:
            self.documents.delete_many(query)
        except:
            print("delete failed")
        else:
            print("delete successed")

    def update(self, query, new_values):
        try:
            self.documents.update_many(query, new_values)
        except:
            print("update failed")
        else:
            print("update successed")
