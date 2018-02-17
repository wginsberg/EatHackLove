from flask import Flask
app = Flask(__name__)


@app.route('/give-suggestion')
def suggestion():
    return "eat more veggies"


@app.route('/post-form')
def submit_data():
    return "post-form"


@app.route('/get-input')
def suggestion():
    return "eat more veggies"
