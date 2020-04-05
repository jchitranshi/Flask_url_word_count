import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config.from_pyfile('config.py')
#app.config.from_object(os.environ['APP_SETTINGS'])
#print(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///wordcount_dev'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Result

@app.route('/')
def hello():
	return "Hello!!"

@app.route('/<name>')
def hello_name(name):
	return "Hello {}!".format(name)

if __name__=='__main__':
	app.run(debug=True)

