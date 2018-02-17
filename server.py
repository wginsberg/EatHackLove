from flask import Flask
from flask_bootstrap import Bootstrap
import pandas as pd
from flask import render_template
from flask import request
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
import googlemaps
from datetime import datetime
import pprint
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main_page.jinja')


@app.route('/assessment', methods=['POST'])
def triage():
    return render_template('final_page.jinja')
