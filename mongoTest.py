import json
import pymongo
from bson import json_util

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DB_NAME = 'AuDaily'
COLLECTION_NAME = 'DailyCost'


def get_datas():
    connection = pymongo.MongoClient(MONGODB_HOST, MONGODB_PORT)
    # connection = pymongo.MongoClient("mongodb://localhost:27017/")
    print(connection.list_database_names())
    collection = connection[DB_NAME][COLLECTION_NAME]

    projects = collection.find()
    # projects = connection["AuDaily"]["DailyCost"].find()

    query = {"year": 2022, "day": 23}
    result = collection.find(query)
    print("=================")
    print(" ")
    for x in result:
        print(x["_id"])
        print(x)

    print(" ")
    print("=================")

    print(type(projects))
    json_projects = []

    for project in projects:
        print(project)
        json_projects.append(project)
        print(type(project))

    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects


def insert_data(year, month, day, cost):
    connection = pymongo.MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DB_NAME][COLLECTION_NAME]
    # newData = {"_id": 20221023, "year": 2022,
    #            "month": 10, "day": 23, "cost": 25}
    # x = collection.insert_one(newData)
    # x.inserted_id to check: _id
    # print(x.inserted_id)


if __name__ == "__main__":
    print(get_datas())
