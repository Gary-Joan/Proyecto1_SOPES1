import os
from flask import Flask, redirect, url_for, request, render_template, jsonify
from pymongo import MongoClient
from json import loads, dumps
from bson import json_util

app = Flask(__name__)
client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017,username='root',password='rootpassword')
db = client["dbproyecto1"]
mycol= db["publicaciones"]

@app.route('/')
def home():
   return "<h2>API SERVIDOR A</h2>"

@app.route('/memoria')
def memoria():
    arry =os.popen('cat /proc/memoria_200915609').read()
    memoria = loads(arry)
    return memoria
@app.route('/cpu')
def cpu():
    arry = os.popen('cat /proc/cpu_200915609').read()
    cpu = loads(arry)
    return cpu  
   


@app.route('/items')
def items():
   
    _items = mycol.find()
    items = [item for item in _items]
    lista = dumps(items,default=json_util.default)
    return lista
   
@app.route('/new', methods=['POST'])
def new():
    data = request.get_json()
    #print(data['autor'],flush=True)
    item_doc = {
        "autor": data['autor'],
        "nota": data['nota']
    } 
    x = mycol.insert_one(item_doc)
    return str(x.inserted_id)
@app.route('/count')
def contador():
    _items = mycol.find()
    items_count={"cantidad ": _items.count()}
    return loads(dumps(items_count))
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80, debug=True)
