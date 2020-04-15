
#client = pymongo.MongoClient("mongodb+srv://1867CAUTHOR:<password>@cluster0-txer5.mongodb.net/test?retryWrites=true&w=majority")
#db = client.test

import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

db = client.test_database # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

collection = db.pokemon_test # "pokemon_test" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

collection.insert_one({
    "name": "Pikachu",
    "level": 30,
    "exp": 76000000000,
    "hp": 400,
})
print("DOCS:", collection.count_documents({}))
print(collection.count_documents({"name": "Pikachu"}))
#inserts record (document) into our collection

#query the collection, get results, then loop through the results 

pikas = list(collection.find({"name": "Pikachu"}))
for pika in pikas:
    print(pika["name"])

#insert multiple documents at the same time
tyranitar = {
    "name": "Tyranitar",
    "level": 77,
    "exp": 4814810,
    "hp": 264,
    "defense": 198,
    "attack": 235
}

psyduck = {
    "name": "Psyduck",
    "level": 20,
    "exp": 23000000,
    "hp": 100,
}

pelipper = {
    "name": "Pelipper",
    "level": 100,
    "exp": 1000000,
    "hp": 324,
    "atk": 122,
    "def": 328,
    "spa": 226,
    "spd": 177,
    "spe": 166,
    "nature": "Bold",
    "ability": "Drizzle",
    "held_item": "Damp Rock",
    "move1": "U-turn",
    "move2": "Scald",
    "move3": "Roost",
    "move4": "Hurricane",
    "hpev": 252,
    "defev": 252,
    "spdev": 6,
    "hpiv": 31,
    "atkiv": 31,
    "defiv": 31,
    "spaiv": 31,
    "spdiv": 31,
    "speiv": 31,
}

never = {
    "name": "NEVER played this game",
    "level": -500,
    "exp": -10000000000009,
    "hp": "a string here, not an int",
}

mewtwo = {
    "name": "Mewtwo",
    "lvl": 20,
    "exp": 23000000,
    "hp": "100",
}

team = [tyranitar, psyduck, pelipper, never, mewtwo]
collection.insert_many(team)
print("DOCS:", collection.count_documents({}))

high_levels = list(collection.find({"level": {"$gte": 70}}))
for doc in high_levels:
    print(doc["name"])

breakpoint()
