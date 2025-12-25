from flask import Flask, render_template 
import os
import requests

BACKEND_URL = os.environ.get('BACKEND_URL', 'http://localhost:8000')

app = Flask(__name__)

PORT = os.environ.get('PORT' , 9000)


@app.route('/')
def home():

    response = requests.get(f"{BACKEND_URL}/api/get")
    data = response.json()
    env= dict(os.environ)
    
    return render_template("index.html", env = env, data=data['data'])

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=PORT ,debug= True)        
