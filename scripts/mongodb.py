import datetime
import json
import os

import bcrypt
from flask import session
from pymongo import MongoClient

if "credentials.json" not in os.listdir('.'):
    data = {"mongo_URI" : os.environ['mongo_URI']}

else:
    data = json.load(open("credentials.json", "r"))

client = MongoClient(data["mongo_URI"])

def log(action, ip, username, incoming, outgoing, status):
    collection = client.asteria.logs
    entry = {"username":username.lower(), "action":action, "ip": ip, "incoming": incoming, "outgoing":outgoing, "status":status, "timestamp": datetime.datetime.utcnow()}
    collection.insert_one(entry)
    client.close()
    return True

def get_list_users():
    collection = client.asteria.usercred
    result = list(collection.find({}, {"username": 1}))
    username_list = list(map(lambda x: x['username'], result))
    return list(username_list) 