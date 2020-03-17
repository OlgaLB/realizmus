#!/usr/bin/env python3

import os
import mysql.connector

from lib.fibonacci_metric import Fibonacci_Metric
from lib.credentials import Connection


def create_database(filename):
    """Read queries from file and run then with MySQL.
       
       Parameters
        ----------
        filename : str
            Path to the filename (inclusive) with queries.
    """
    conn = mysql.connector.connect(host=Connection.MYSQL_HOST, user=Connection.MYSQL_USER_ROOT, password = Connection.MYSQL_PASSWORD_ROOT)
    cursor = conn.cursor()

    queries_list = []
    with open(filename) as queries_file:
        queries = queries_file.read()
        queries_list = queries.split(';\n')
        queries_list = list(filter(None, queries_list))

    for query in queries_list:
        cursor.execute(query)

    cursor.close()
    conn.close()


def populate_table(request, response):
    """Populate table (fibonacci_metrics) by requests and responses.

        Parameters
        ----------
        request : str
            Sent request.
        response: int
            Response code.
    """
    create_database(os.path.join('db', 'fibonacchi_db_v1.0.0.sql'))
    conn = mysql.connector.connect(user=Connection.MYSQL_USER, password=Connection.MYSQL_PASSWORD,
                              host=Connection.MYSQL_HOST,
                              database=Connection.MYSQL_DB)
    cursor = conn.cursor()
    
    fibonacci_metrics = Fibonacci_Metric(request, response)

    query = f'INSERT INTO fibonacci_metrics (request, response) VALUES (\'{fibonacci_metrics.request}\', {fibonacci_metrics.response});'

    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()
