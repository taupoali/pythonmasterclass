from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.customers

# find_one gives me one document back as a python dict
the_contacts = db.contacts.find_one({})
print(type(the_contacts))
print(the_contacts)

print("Let's try and get all the documents in the collection")
all_the_contacts = db.contacts.find({})
for contact in all_the_contacts:
    print(contact)
