#!/usr/bin/env python3


MIN_FIB_VALUE = 2


def fibonacci(number_from, number_to):
    """Create array of Fibonacci numbers between (inclusive) number_from and number_to.

        Parameters
        ----------
        number_from : int
            Min value.
        number_to: int
            Max value.

        Returns:
        ----------
        array of int
            Array of Fibonacci numbers between (inclusive) number_from and number_to.
    """
    previous_value = 0
    fibonacci_values = []
    current_value = 1
 
    while True:
        temp_value = current_value
        current_value += previous_value
        previous_value = temp_value
        if current_value < number_from:
            continue
        fibonacci_values.append(current_value)
        if (current_value + previous_value > number_to):
            break

    return fibonacci_values


def find_array(maximum_value, search_array):
    """Finds array of combinations of search_array parameter up to maximum_value.

        Parameters
        ----------
        maximum_value : int
            Given number, up to which combinations to be found.
        search_array: array of int
            Array of numbers to search in.

        Returns:
        ----------
        array of arrays of int
            Array of unique array combinations.
    """
    if maximum_value < MIN_FIB_VALUE:
        return []
    
    combinations = []

    for current_value in reversed(search_array):

        if current_value < MIN_FIB_VALUE:
            return []

        if current_value == maximum_value:
            combinations.append([current_value]) 

        new_value = maximum_value - current_value

        if new_value in combinations:
            continue
   
        temp_array = find_array(new_value, search_array)
        if len(temp_array) > 0:
            combinations += list(map(lambda x: x + [current_value], temp_array))
    
    distinct_array = []

    for sub_array in combinations:
        sub_array.sort(reverse = True)
        if sub_array not in distinct_array:
            distinct_array.append(sub_array)

    return distinct_array


def create_series(number):
    """Finds array of combinations up to number from Fibonacci array between (inclusive) MIN_FIB_VALUE and number.

        Parameters
        ----------
        number : int
            Given number, up to which combinations to be found.
        
        Returns:
        ----------
        array of arrays of int
            Array of unique array combinations.
    """
    return find_array(number, fibonacci(MIN_FIB_VALUE, number))
