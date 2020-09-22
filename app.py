import os
from flask import Flask, redirect, url_for, request, render_template, jsonify
from pymongo import MongoClient
app = Flask(__name__)
client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017,username='root',password='rootpassword')
db = client["dbproyecto1"]
mycol= db["publicaciones"]

@app.route('/')
def todo():
   return "<h2>API SERVIDOR A</h2>"

@app.route('/memoria')
def hello():
    arry =os.popen('cat /proc/memoria_200915609').read()
    memoria = loads(arry)
    return memoria
@app.route('/cpu')
def cpu():
    arry = os.popen('cat /proc/cpu_200915609').read()
    cpu = loads(arry)
    return cpu  
   

@app.route('/items')
def todo():
    collist = mycol.list_collection_names()
    _items = {}
    if "publicaciones" in collist:
        _items = mycol.find()
        listapublicaciones = loads(_items)
        return listapublicaciones

    else:
        return "Error columna de datos no existe!!"


@app.route('/new')
def new():
    item_doc = {
        'name': request.form['name'],
        'description': request.form['description']
    }
    print(request.form)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80, debug=True)
