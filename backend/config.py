from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS #cross origin request, send request to backend from a diff url

#init flask app
app = Flask(__name__)
CORS(app)

#init databases, location of db data
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

#create instance of the db giving access for crud funcs
db = SQLAlchemy(app)