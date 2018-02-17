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


@app.route('/calculate-test', methods=['GET'])
def calculate_test():
    data = [{   
                'store': 'MTR',
                'total': 12.99,
                'basket': [
                        {'name': 'oatmeal', 'serving': ' 2 x 100g'},
                        {'name': 'olive oil', 'serving': ' 1 x 15ml'}
                ]
            },
            {
                'store': 'NF',
                'total': 14.25,
                'basket': [
                        {'name': 'oatmeal', 'serving': ' 2 x 100g'},
                        {'name': 'olive oil', 'serving': ' 1 x 15ml'}
                ]
            },
            {
                'store': 'LBW',
                'total': 14.99,
                'basket': [
                        {'name': 'oatmeal', 'serving': ' 2 x 100g'},
                        {'name': 'olive oil', 'serving': ' 1 x 15ml'}
                ]
            }
    ]
    return render_template('final_page.jinja', data=data)

@app.route('/calculate', methods=['POST'])
def calculate():
    input = request.form
    print(input)
    calories = int(input['carbs']) * 4 + int(input['fat']) * 9 + int(input['protein']) * 4
    with open('bulking-a', 'w') as f:
        f.write("{},{},{},{}\n".format(
            "~" + str(calories),
            "~" + input['carbs'],
            ">" + input['fat'],
            ">" + input['protein']
            ))
    data = budget_calc.main("food-db", "bulking-a")
    return render_template('final_page.jinja', data=data)
