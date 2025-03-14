#! C:\Users\chrst\OneDrive\Documents\GitHub\NumPySymPy-Assignment\myenv\Scripts\python.exe

import numpy as np

def is_subset(set_a, set_b):
    return np.all(np.isin(set_a, set_b))
    
set_a = {1,3,5}
set_b = {2, 1, 4, 3, 6, 5}

print("Is set_a a subset of set_b? ", is_subset(set_a, set_b))