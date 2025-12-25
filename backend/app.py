from flask import Flask, render_template , jsonify
import os
from connection import collections
app = Flask(__name__)

PORT = os.environ.get('PORT' , 8000)
@app.route('/')
def home():
    return jsonify({"message": "Fenrir Backend is running"})

@app.route('/api/get')
def api():
    names = collections.find()
    result = []

    for name in names:

        result.append(name['value'])

    result = {      
            'data': result}

    return jsonify(result)

@app.route('/api/add/<name>')               
def add(name):

    collections.insert_one({'value': name})
    return jsonify({"message": "Added"})

 

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=PORT ,debug=True)        
