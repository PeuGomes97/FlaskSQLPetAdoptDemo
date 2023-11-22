"""Flask App for Adopt"""

from flask import Flask, url_for, render_template, redirect, flash, jsonify

# from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt_db"

connect_db(app)
db.create_all()

# toolbar = DebugToolbarExtension(app)
