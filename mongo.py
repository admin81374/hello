import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["BigData"]
collection = mydb["student"]
data = {"Name": "", "Department": "IT"}
collection.insert_one(data) 
print("Database and collection created successfully") 



import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["BigData"]
print(client.list_database_names())
collection = mydb["student"]
collection.delete_many({})
print("Old Records Deleted!")
mylist = [
    {"name":"","Department":"IT"},
    {"name":"","Department":"Science"},
    ]
x=collection.insert_many(mylist)
print(mydb.list_collection_names())



import pymongo
client= pymongo.MongoClient("mongodb://localhost:27017/")
print("client")
mydb=client["BigData"]
print(client.list_database_names())
collection=mydb["student"]
alldocs=collection.find()
for item in alldocs:
    print(item)



import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)
mydb = client["BigData"]
print(client.list_database_names())
collection = mydb["student"]
collection.delete_one({"name": ""})
alldocs=collection.find()
for item in alldocs:
    print(item)



import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)
mydb = client["BigData"]
print(client.list_database_names())
collection = mydb["student"]
collection.update_one({'name': ''},
{'$set': {'Department': 'CS'}})
alldocs = collection.find()
for item in alldocs:
    print(item)







