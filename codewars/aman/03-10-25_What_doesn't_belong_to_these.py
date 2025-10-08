"""
Question Link : https://www.codewars.com/kata/583dee7395a0632356000a0f/train/python
<| 5 kyu |> | 03rd Oct '25
What doesn't belong to these?

Introduction
#What doesn't belong to these?

Write a method that takes an array of elements and returns the element that does not belong to these elements.

Example:

[1, 2, 2, 2, 2] -> 1
['1', 2, '4', '6', '8'] -> 2
[2, 2, -2, 6, 10] -> -2
['a', 'a', 'b', 'a', 'a', 'a', 'a'] -> 'b'
Look in the example tests. (The submit tests have no additional surprises!)

The elements will only be of the types:
boolean, char (or string with one char in JS/TS) or int (number in JS/TS).

The array will never be null and there will always more than 2 values in the array!

It is always exactly one element that does not belong to the other elements.
The values in the array will never be null or undefined or 0.

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have also created other katas. Take a look if you enjoyed this kata!
"""

# SOLUTION
def check_for_odd_data_type(series):
    type_dict = {}
    for item in series:
        type_dict.setdefault(type(item), []).append(item)

    if len(type_dict) > 1:
        return min(type_dict.values(), key=len)[0]
    
    # STRINGS
    if all([isinstance(item, str) for item in series]):
        for item in series:
            if not item.isalpha():
                return item
        lower_count = sum([item.islower() for item in series ])
        upper_count = len(series)-lower_count
        if lower_count == 1:
            return next(i for i in series if i.islower())
        if upper_count == 1:
            return next(i for i in series if i.isupper())
    
    # Booleans
    if all([isinstance(item, bool) for item in series]):
        for item in series:
            if series.count(item) == 1:
                return item
    # Integer
    if all([isinstance(item, int) for item in series]):
        rem_check = [item%2 for item in series]
        if len(set(rem_check)) > 1:
            least_index = rem_check.index(min(rem_check, key=rem_check.count))
            return series[least_index]
        positive_count = sum([item >0 for item in series ])
        negative_count = len(series)-positive_count
        if positive_count == 1:
            return next(i for i in series if i > 0)
        if negative_count == 1:
            return next(i for i in series if i < 0)
    
    # FallBack 
    for item in series:
        if series.count(item) == 1:
            return item

def find_the_not_fitting_element(series):
    return check_for_odd_data_type(series)

# -Solution END-

# INPUT
>>> find_the_not_fitting_element([2, 2, 2, 2, 2, '2'])

# OUTPUT
>>> "2"

# INPUT
>>> find_the_not_fitting_element([1, 2, 4, 6, True])

# OUTPUT
>>> True