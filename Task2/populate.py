#!/usr/bin/env python3

import os
import mysql.connector

from lib.fibonacci_metric import Fibonacci_Metric
from lib.credentials import Connection


def populate_table(number, array):
    """Populate table (fibonacci_metrics) by requests and responses.

        Parameters
        ----------
        request : str
            Sent request.
        response: int
            Response code.
    """
    conn = mysql.connector.connect(user=Connection.MYSQL_USER, password=Connection.MYSQL_PASSWORD,
                              host=Connection.MYSQL_HOST,
                              database=Connection.MYSQL_DB)
    cursor = conn.cursor()
    
    fibonacci_metrics = Fibonacci_Metric(request, response)

    query = f'INSERT INTO fibonacci_sequence (request, response) VALUES (\'{fibonacci_metrics.request}\', {fibonacci_metrics.response});'

    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()
