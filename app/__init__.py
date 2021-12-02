import os
from flask import Flask, render_template, request
from flask_bcrypt import Bcrypt
from flaskext.mysql import MySQL
from flask_session import Session
# from flask_login import LoginManager



app = Flask(__name__)
mysql = MySQL()
app.config['SECRET_KEY'] = 'urip kaya kiye temen yah'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = ''
# app.config['MYSQL_DATABASE_DB'] = 'sdc_cnn'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['UPLOAD_FOLDER'] = os.path.abspath('app/static/upload/wisata')
bcrypt = Bcrypt(app)


app.config['MYSQL_DATABASE_USER'] = os.getenv("DB_USER")
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv("DB_PASS")
app.config['MYSQL_DATABASE_DB'] = os.getenv("DB_NAME")
app.config['MYSQL_DATABASE_HOST'] = os.getenv("DB_HOST")
mysql.init_app(app)

from app.controllers import admincontroller
from app.controllers import indexcontroller
from app.controllers import logincontroller
from app.controllers import satgascontroller
