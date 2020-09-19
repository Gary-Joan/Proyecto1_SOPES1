import os
from flask import Flask, redirect, url_for, request, render_template, jsonify
from pymongo import MongoClient
app = Flask(__name__)
client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017,username='root',password='rootpassword')
db = client.tododb
@app.route('/hello')
def hello():
    arry =[]
    arry =os.popen('cat /proc/version').read()
    return jsonify(arry)
@app.route('/')
def todo():
    _items = db.tododb.find()
    items = [item for item in _items]
    return render_template('todo.html', items=items)
@app.route('/new', methods=['POST'])
def new():
    item_doc = {
        'name': request.form['name'],
        'description': request.form['description']
    }
    db.tododb.insert_one(item_doc)
    return redirect(url_for('todo'))
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80, debug=True)
