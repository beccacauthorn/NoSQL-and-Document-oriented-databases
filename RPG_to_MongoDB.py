import os
from dotenv import load_dotenv
import sqlite3
import pandas as pd
import pymongo

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

# connect to sqlite db
conn_sqlite = sqlite3.connect('rpg_db.sqlite3')
print(type(conn_sqlite))

# read a table from sqlite DB
sqlite_c = conn_sqlite.cursor()
results = sqlite_c.execute('SELECT * FROM charactercreator_character').fetchall()
print(results[:5])

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

db = client.RPG_database # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

collection = db.characters # "pokemon_test" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)

# get all rows
results = sqlite_c.execute('SELECT * FROM charactercreator_character').fetchall()

# take a row one by one and convert it to a dict
#for row in results:
#    dict_from_row = {'character_id': row[0], 'name': row[1], 'level': row[2],
#    'exp': row[3], 'hp': row[4], 'strength': row[5], 
#    'intelligence': row[6], 'dexterity': row[7], 'wisdom': row[8]}
#    # add the dict
#    collection.insert_one(dict_from_row)

# take all rows, convert them ALL to dicts
documents = []
for row in results:
    dict_from_row = {'character_id': row[0], 'name': row[1], 'level': row[2],
    'exp': row[3], 'hp': row[4], 'strength': row[5], 
    'intelligence': row[6], 'dexterity': row[7], 'wisdom': row[8]}
    # add to the list
    documents.append(dict_from_row)

# add all dicts
collection.insert_many(documents)

# sanity check: print number of documents
print("----------------")
print("NUMBER OF DOCUMENTS:")
print(collection.count_documents({}))
