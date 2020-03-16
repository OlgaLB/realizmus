#!/usr/bin/env python3

import pytest
import requests


#def test_check_intermediate_fib():
#    response = requests.get('http://127.0.0.1:5000/fib/13')
#    assert response.status_code == 200
#    assert response.content == '[[13], [8, 5], [8, 3, 2], [5, 5, 3], [5, 3, 3, 2], [5, 2, 2, 2, 2], [3, 3, 3, 2, 2], [3, 2, 2, 2, 2, 2]]'

#def test_check_minimum_fib():
#    response = requests.get('http://127.0.0.1:5000/fib/2')
#    assert response.status_code == 200
#    assert response.content == '[[2]]'

#def test_check_small_fib():
#    response = requests.get('http://127.0.0.1:5000/fib/3')
#    assert response.status_code == 200
#    assert response.content == '[[3]]'

#def test_check_negative():
#    response = requests.get('http://127.0.0.1:5000/fib/-1')
#    assert response.status_code == 200
#    assert response.content == '[]'

#def test_check_zero():
#    response = requests.post('http://127.0.0.1:5000/fib/0')
#    assert response.status_code == 200
#    assert response.content == '[]'

#def test_check_float():
#    response = requests.get('http://127.0.0.1:5000/fib/13.5')
#    assert response.status_code == 200
#    assert response.content == '[]'

#def test_check_letter():
#    response = requests.get('http://127.0.0.1:5000/fib/a')
#    assert response.status_code == 200
#    assert response.content == '[]'
