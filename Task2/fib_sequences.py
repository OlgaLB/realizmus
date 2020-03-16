#!/usr/bin/env python3


MIN_FIB_VALUE = 2


def fibonacci(number_from, number_to):
    previous_value = 0
    result = []
    value = 1
 
    while True:
        temp_value = value
        value += previous_value
        previous_value = temp_value
        if value < number_from:
            continue
        result.append(value)
        if (value + previous_value > number_to):
            break

    return result


def find_array(value, array):
    if value < MIN_FIB_VALUE:
        return []
    
    return_array = []

    for item in reversed(array):

        if item < MIN_FIB_VALUE:
            return []

        if item == value:
            return_array.append([item]) 

        new_value = value - item

        if new_value in return_array:
            continue
   
        temp_array = find_array(new_value, array)
        if len(temp_array) > 0:
            return_array += list(map(lambda x: x + [item], temp_array))
    
    distinct_array = []

    for sub_array in return_array:
        sub_array.sort(reverse=True)
        if sub_array not in distinct_array:
            distinct_array.append(sub_array)

    return distinct_array


def create_series(number):
    return find_array(number, fibonacci(MIN_FIB_VALUE, number))
