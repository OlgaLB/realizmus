#!/usr/bin/env python3

import pytest
import requests
import populate


def test_check_intermediate_fib():
    path = 'http://127.0.0.1:5000/fib/13'
    response = requests.get(path)
    populate.populate_table(path, response.status_code)
    assert response.status_code == 200
    assert response.content.decode("utf-8") == '[[13], [8, 5], [8, 3, 2], [5, 5, 3], [5, 3, 3, 2], [5, 2, 2, 2, 2], [3, 3, 3, 2, 2], [3, 2, 2, 2, 2, 2]]'

def test_check_minimum_fib():
    path = 'http://127.0.0.1:5000/fib/2'
    response = requests.get(path)
    populate.populate_table(path, response.status_code)
    assert response.status_code == 200
    assert response.content.decode("utf-8") == '[[2]]'

def test_check_small_fib():
    path = 'http://127.0.0.1:5000/fib/3'
    response = requests.get(path)
    populate.populate_table(path, response.status_code)
    assert response.status_code == 200
    assert response.content.decode("utf-8") == '[[3]]'

def test_check_negative():
    path = 'http://127.0.0.1:5000/fib/-1'
    response = requests.get(path)
    populate.populate_table(path, response.status_code)
    assert response.status_code == 200
    assert response.content.decode("utf-8") == '[]'

def test_check_zero():
    path = 'http://127.0.0.1:5000/fib/0'
    response = requests.get(path)
    populate.populate_table(path, response.status_code)
    assert response.status_code == 200
    assert response.content.decode("utf-8") == '[]'

def test_check_float():
    path = 'http://127.0.0.1:5000/fib/13.5'
    response = requests.get(path)
    populate.populate_table(path, response.status_code)
    assert response.status_code == 200
    assert response.content.decode("utf-8") == '[]'

def test_check_letter():
    path = 'http://127.0.0.1:5000/fib/a'
    response = requests.get(path)
    populate.populate_table(path, response.status_code)
    assert response.status_code == 200
    assert response.content.decode("utf-8") == '[]'
