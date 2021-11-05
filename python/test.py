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

# ask a name
#name = input("What's your name ?\n")

# Insert the new user
#collection_name.insert_one({
#    "_id": ObjectId(),
#    "name": name
#})

# Get all the users from the users collection
#users = collection_name.find()
#for user in users:
#        print(user)

# Get a user by name
#name2 = input("Which user do you look for ?\n")
#users = list(collection_name.find({
#    "name": {
#        '$regex':'.*'+name2+'.*',
#        '$options': 'i'
#    }
#}))
#if len(users) <= 0:
#    print("There is no user found !")
#else:
#    print(users)

# Delete rows with toto attributs
#collection_name.delete_many({"toto": {"$exists": True}})

# Update part
#users = list(collection_name.find({}))
#if len(users) <= 0:
#    print("There is no user found !")
#else:
#    for index, user in enumerate(users):
#        print(str(index) + ": for " + str(user.get('name')))

#number = int(input('Which one do you want to update ?\n'))
#new_name = input('New name ?\n')

#for index, user in enumerate(users):
#    if index == number:
#        id = user.get('_id')

#collection_name.update_one({"_id": id}, {
#    "$set": {
#        "name": new_name
#    }
#})

# Delete part
users = list(collection_name.find({}))
if len(users) <= 0:
    print("There is no user found !")
else:
    for index, user in enumerate(users):
        print(str(index) + ": for " + str(user.get('name')))

number = int(input('Which one do you want to delete ?\n'))

for index, user in enumerate(users):
    if index == number:
        id = user.get('_id')

collection_name.delete_one({"_id": id})