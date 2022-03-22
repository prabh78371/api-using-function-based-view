from flask import request
import requests
import json


def post_data():
    URL = "http://127.0.0.1:8000/create/"
    data = {'name':'harman',
    'rollno' : 11801019,
    'designation':'engineer '}

    json_data = json.dumps(data)
    r = requests.post(url = URL,data = json_data)
    r_data = r.json()
    print(r_data)

post_data()
def get_data(id=None):
    URL = "http://127.0.0.1:8000/create/"
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL,data = json_data)
    data = r.json()
    print(data)

# get_data(1)
def update_data():
    URL = "http://127.0.0.1:8000/create/"
    data = {'id': 4,
    'name':'raman',
    'designation': 'docter'}
    json_data = json.dumps(data)
    r =requests.put(url = URL,data = json_data)
    data = r.json()
    print(data)
# update_data()

def delete_data():
    URL = "http://127.0.0.1:8000/create/"
    data = {'id': 1}
    json_data = json.dumps(data)
    r = requests.delete(url = URL,data = json_data)
    data = r.json()
    print(data)
# delete_data()

