#!/usr/bin/env python3

import os

from flask import Flask, request
from healthcheck import HealthCheck

import populate
import fib_sequences


app = Flask(__name__)

health = HealthCheck(app, "/healthcheck")

def health_check():
    response = requests.get('http://127.0.0.1:5000/healthcheck')

health.add_check(health_check)

@app.route('/fib/<number>', methods=['GET'])
def form_sequences(number):
    if (number.isdigit() or number.isdecimal()):
        if int(number) <= 0:
            return str([])
    #    # populate.populate_table(request.path, status_code)
        return str(fib_sequences.create_series(int(number)))
    else:
        return str([])
   
@app.route('/health', methods=['GET'])
def health():
    health_check()


if __name__ == "__main__":
    app.run()
