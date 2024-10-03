# database.py
from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGO_URL"))
db = client["btg_pactual"]

# Colecciones
users_collection = db["users"]
funds_collection = db["funds"]
transactions_collection = db["transactions"]
