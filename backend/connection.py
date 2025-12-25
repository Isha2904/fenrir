#mongo db connection
from pymongo import MongoClient
import os

MONGO_HOST = os.environ.get('MONGO_HOST' , 'localhost')
client = MongoClient(MONGO_HOST, 27017)

db = client["fenrir_db"]
collections = db["names"]