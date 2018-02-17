from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/get-suggestion')
def give_suggestion():
    return "eat more veggies"


@app.route('/sign-up', methods=['POST'])
def sign_up():
    result = request.form
    print(result)
    return "Hey"


@app.route('/give-input', methods=['POST'])
def get_input():
    input = request.form
    print(input)
    return "I want to eat more veggies"
