import numpy as np

def cartesian_product(*arrays):
    grid = np.meshgrid(*arrays)
    cartesian = np.stack(grid, axis=-1).reshape(-1, len(arrays))
    return cartesian

main_dishes = ['Burger', 'Pizza']
sides = ['Fries', 'Salad']
drinks = ['Soda', 'Water']

meal_combinations = cartesian_product(main_dishes, sides, drinks)
print(meal_combinations)