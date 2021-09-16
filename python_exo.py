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

# Get all the publication of type Book
anwser1 = str(collection_name.count_documents({"type" : "Book"}))
print(anwser1)

# Get all the publication of type Articles
anwser2 = str(collection_name.count_documents({"type" : "Article"}))
print(anwser2)

anwser3 = str(collection_name.count_documents({"year" : {
    '$gt': 2011
}}))
print(anwser3)

anwser4 = list(collection_name.find({"type" : "Book", "year" : {
    '$gt': 2014
}}))
print(anwser4)

anwser5 = list(collection_name.find({"authors" : "Toru Ishida"}))
print(anwser5)

anwser6 = list(collection_name.distinct("publisher"))
print(anwser6)

anwser7 = list(collection_name.distinct("authors"))
print(anwser7)