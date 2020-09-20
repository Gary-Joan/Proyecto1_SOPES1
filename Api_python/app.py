import os
from flask import Flask, redirect, url_for, request, render_template, jsonify
app = Flask(__name__)
@app.route('/hello')
def hello():
    return "hola Mundo"
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80, debug=True)
