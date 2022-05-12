from django.shortcuts import render
from flask import Flask,redirect,render_template

app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")