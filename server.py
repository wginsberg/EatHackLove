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
import budget_calc
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main_page.jinja')


@app.route('/calculate', methods=['POST'])
def calculate():
    print(request.form)
    data = budget_calc.main("food-db", "bulking-a")
    print(data)
    return render_template('final_page.jinja', data=data)
