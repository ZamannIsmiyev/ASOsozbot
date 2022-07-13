from pymongo import MongoClient

from config import MONGO_URI

client = MongoClient(mongodb+srv://aylak:aylak@cluster0.cd5my.mongodb.net/Cluster0?retryWrites=true&w=majority)
database = client.ASOsozutap_bot
