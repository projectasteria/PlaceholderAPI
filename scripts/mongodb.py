import datetime
import json
import os

import bcrypt
from flask import session
from pymongo import MongoClient

if "credentials.json" not in os.listdir('.'):
    data = {"mongo_username" : os.environ['mongo_username'], "mongo_password": os.environ['mongo_password'], "mongo_ip": os.environ['mongo_ip'], "mongo_port": os.environ['mongo_port']}

else:
    data = json.load(open("credentials.json", "r"))

def log(action, ip, username, incoming, outgoing, status):
    client = MongoClient("mongodb://{}:{}@{}:{}".format(data["mongo_username"], data["mongo_password"], data["mongo_ip"], data["mongo_port"]))
    collection = client.asteria.logs
    entry = {"username":username.lower(), "action":action, "ip": ip, "incoming": incoming, "outgoing":outgoing, "status":status, "timestamp": datetime.datetime.utcnow()}
    collection.insert_one(entry)
    client.close()
    return True

def get_list_users():
    client = MongoClient("mongodb://{}:{}@{}:{}".format(data["mongo_username"], data["mongo_password"], data["mongo_ip"], data["mongo_port"]))
    collection = client.asteria.usercred
    result = list(collection.find({}, {"username": 1}))
    username_list = list(map(lambda x: x['username'], result))
    return list(username_list) 