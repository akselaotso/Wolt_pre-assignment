import pytest
import json
from delivery_cost_calculator.Modules.cost_calculator import cost_calculator_class as c

def test_cost_calculator():
    test_data_file = open('tests/calculator_test.json')
    test_values_and_results = json.load(test_data_file)
    test_data_file.close()

    for set in test_values_and_results.values():
        delivery = c.cost_calculator(set['cart_value'], set['delivery_distance'], set['number_of_items'], set['time'])
        assert delivery.final_price() == set['result']

