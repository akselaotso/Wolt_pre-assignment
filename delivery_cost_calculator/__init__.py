from flask import (Flask, request)
import json
from .Modules.cost_calculator import cost_calculator_class as c

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['POST'])
    def home_page():

        if not request.is_json:
            return "400 Bad Request: The request did not contain JSON.\n"

        data = request.get_json()

        value = data["cart_value"]
        distance = data["delivery_distance"]
        items = data["number_of_items"]
        time = data["time"]

        delivery = c.cost_calculator(value, distance, items, time)

        fee = delivery.final_price()

        package_fee = {'delivery_fee': fee}

        return json.dumps(package_fee)

    return app

