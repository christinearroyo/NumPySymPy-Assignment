#! C:\Users\chrst\OneDrive\Documents\GitHub\NumPySymPy-Assignment\myenv\Scripts\python.exe
'''
import numpy as np

def is_subset(set_a, set_b):
    
    array_a = np.array(list(set_a))
    array_b = np.array(list(set_b))

    result = np.isin(array_a, array_b).all()
    return result
    
set_a = {1,3,5}
set_b = {2, 1, 4, 3, 6, 5}

print("Is set_a a subset of set_b? ", is_subset(set_a, set_b))
'''

