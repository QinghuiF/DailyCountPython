import mongoHelper


class DailyCost:
    def __init__(self):
        self.mongoConnecter = mongoHelper.MongoHelper('localhost', 27017, 'AuDaily', 'DailyCost')
        self.mongoConnecter.mongo_connect()

    def find(self, query):
        documents = self.mongoConnecter.find(query)
        return documents


def main():
    daily_cost = DailyCost()
    # daily_cost.mongoConnecter.mongo_connect()
    # documents = daily_cost.mongoConnecter.find({})
    # newData = {"_id": 20221106, "year": 2022, "month": 11, "day": 6, "cost": 45}
    # daily_cost.mongoConnecter.insert_one_data(newData)
    # daily_cost.mongoConnecter.delete_one_data({"year":2022, "month": 11})
    query = {}
    documents = daily_cost.find(query)
    print(type(documents))
    for i in documents:
        print(type(i))
        print(i)


if __name__ == "__main__":
    main()
