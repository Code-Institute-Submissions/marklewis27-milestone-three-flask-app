from flask import Flask
from datetime import datetime
from flask import render_template
from flask_pymongo import PyMongo

import re

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb+srv://me:Internal27@myfirstcluster-x6esz.mongodb.net/task_manager?retryWrites=true&w=majority'

mongo= PyMongo(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")    

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")