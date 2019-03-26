from flask import Flask, jsonify, render_template, redirect, url_for, flash
from flask import request
from flask import session as login_session
from sqlalchemy import Column, ForeignKey, Integer, String

#from models import Base, Category, Item, User

#import os
#os.environ['PYTHON_EGG_CACHE'] = '/usr/local/pylons/python-eggs' 


app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello, I love Digital Ocean!"
if __name__ == "__main__":
    app.run()

