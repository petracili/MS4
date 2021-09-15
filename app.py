import os

from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
if os.path.exists("env.py"):
    import env


# flask
app = Flask(__name__)

# mondodb
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/champion")
def champion():
    chempion_list = list(mongo.db.chempion.find())
    return render_template("champion.html", chempion_list=chempion_list) 

@app.route("/puppy")
def puppy():
    bully_list = list(mongo.db.bully.find())
    return render_template("puppy.html", bully_list=bully_list) 

@app.route("/contact")
def contact():
    return render_template("contact.html") 




if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)