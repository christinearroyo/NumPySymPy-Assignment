#! C:\Users\chrst\OneDrive\Documents\GitHub\NumPySymPy-Assignment\myenv\Scripts\python.exe

import numpy as np
from sympy import FiniteSet

set_a = {1,3,5,}
set_b = {2, 1, 4, 3, 6, 5}

def is_subset(set_a, set_b): 
    array_a = np.array(list(set_a))
    array_b = np.array(list(set_b))

    result = np.isin(array_a, array_b).all()
    return result

print("Is set_a a subset of set_b? ", is_subset(set_a, set_b))

def powerset(s):
    s = FiniteSet(*s)
    result = []

    for subset in s.powerset():
        result.append(subset)

    return sorted(result)

s = {1, 2, 3}
print(powerset(s))


def cartesian_product(*arrays):
    grid = np.meshgrid(*arrays)
    cartesian = np.stack(grid, axis=-1).reshape(-1, len(arrays))
    return cartesian

main_dishes = ['Burger', 'Pizza']
sides = ['Fries', 'Salad']
drinks = ['Soda', 'Water']

meal_combinations = cartesian_product(main_dishes, sides, drinks)
print(meal_combinations)
