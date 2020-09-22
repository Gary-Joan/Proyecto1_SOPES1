import os
from flask import Flask, redirect, url_for, request, render_template, jsonify
app = Flask(__name__)
@app.route('/')
def hello():
    return "<h2>SERVIDOR 1</h2>"
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80, debug=True)
