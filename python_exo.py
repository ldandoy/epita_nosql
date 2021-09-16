from bson.objectid import ObjectId
from pymongo import MongoClient

# Connection
# CONNECTION_STRING="mongodb+srv://epita:epita@cluster0.28nix.mongodb.net/test?retryWrites=true&w=majority"
CONNECTION_STRING="mongodb://127.0.0.1/retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)

# Data base selection
dbname = client['epita-test']

# Collection selection
collection_name = dbname["publis"]

anwser1 = list(collection_name.find({"type" : "Book"}))
print(anwser1)