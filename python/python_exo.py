from bson.objectid import ObjectId
from pymongo import MongoClient

# Connection
# CONNECTION_STRING="mongodb+srv://epita:epita@cluster0.28nix.mongodb.net/test?retryWrites=true&w=majority"
CONNECTION_STRING="mongodb://127.0.0.1/?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)

# Data base selection
dbname = client['epita-test']

# Collection selection
collection_name = dbname["publis"]

# Get all the publication of type Book
anwser1 = str(collection_name.count_documents({"type" : "Book"}))
# print(anwser1)

# Get all the publication of type Articles
anwser2 = str(collection_name.count_documents({"type" : "Article"}))
# print(anwser2)

# List all the document published since 2011 ;
anwser3 = str(collection_name.count_documents({"year" : {
    '$gt': 2011
}}))
# print(anwser3)

# List all the docmuents (type « Book ») published since 2014 ;
anwser4 = list(collection_name.find({"type" : "Book", "year" : {
    '$gt': 2014
}}))
# print(anwser4)

# List all the docmuents of the autor « Toru Ishida » ;
anwser5 = list(collection_name.find({"authors" : "Toru Ishida"}))
# print(anwser5)

# List all distincts publishers (type « publisher ») ;
anwser6 = list(collection_name.distinct("publisher"))
# print(anwser6)

# List all auteurs distincts ;
anwser7 = list(collection_name.distinct("authors"))
# print(anwser7)

# Sort the publication of « Toru Ishida » by title and by start page ;
anwser8 = list(collection_name.aggregate([
    {"$match":{"authors" : "Toru Ishida"}}, 
    {"$sort" : { "booktitle" : 1, "pages.start" : 1 }}
]))
print(anwser8)

# Count his publications ;
anwser9 = list(collection_name.count_documents({"authors" : "Toru Ishida"}))
# print(anwser9)

# Count the number of publication since 2011 and group by type;
anwser10 = str(collection_name.count_documents({"year" : {'$gt': 2011}}))
# print(anwser10)