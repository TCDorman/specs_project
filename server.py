from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session
# from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db

app = Flask(__name__)

app.secret_key = "314065"

app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    return render_template("homepage.html")
