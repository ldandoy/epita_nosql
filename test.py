from bson.objectid import ObjectId
from pymongo import MongoClient

# Connection
# CONNECTION_STRING="mongodb+srv://epita:epita@cluster0.28nix.mongodb.net/test?retryWrites=true&w=majority"
CONNECTION_STRING="mongodb://127.0.0.1/retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)

# Data base selection
dbname = client['epita-test']

# Collection selection
collection_name = dbname["users"]

# Insert the new user
collection_name.insert_one({
    "_id": ObjectId(),
    "toto": "test"
})

# Get all the users from the users collection
users = collection_name.find()
for user in users:
        print(user)