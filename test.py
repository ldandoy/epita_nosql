from pymongo import MongoClient

CONNECTION_STRING="mongodb+srv://epita:epita@cluster0.28nix.mongodb.net/test?retryWrites=true&w=majority"

client = MongoClient(CONNECTION_STRING)

dbname = client['test']

user = {
    "_id": "UIT",
    "toto": "test"
}

collection_name = dbname["users"]

collection_name.insert_many([user])