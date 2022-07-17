import pymongo
client = pymongo.MongoClient("mongodb+srv://Alonewinner:Alonewinner@cluster0.zm2os.mongodb.net/?retryWrites=true&w=majority")
db = client.test
#client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
#db = client.test
print(db)

# creating dict
d ={
    "name":"shubham",
    "email":"drsn@gmail.com",
    "surname":"chaudhary"

}
d1={
    "name": "sonam",
    "email": "drsona@gmail.com",
    "surname": "chaudhary"

}

db1=client['mongotest']
coll=db1['test']
#coll.insert_one(d)

coll.insert_one(d1)