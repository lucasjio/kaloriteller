import certifi
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import sys

app = FastAPI()
brukernavn = "lucasjio"
passord = "mongodb_Vinterferie22;"
uri = f"mongodb+srv://test:test@kaloriteller.xgvddyj.mongodb.net/?retryWrites=true&w=majority"

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())
mydb = client["mydatabase"]
mycol = mydb["foods"]
food_names = []

@app.get("/food_names")
async def read_items():
    for x in mycol.find({},{"navn": 1, "_id": 0}):
        food_names.append(x["navn"])
    return food_names

@app.get("/food_details/{food_name}")
async def read_item(food_name: str):
    food_details = mycol.find_one({"navn": food_name}, {"_id": 0})
    # food_details = mycol.find_one({"navn": food_name})

   
    return food_details


try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)












