
"""
import numpy as np

set_a = {1, 3, 5}
set_b = {2, 1, 4, 3, 6, 5}

def is_subset(set_a, set_b):
    return np.isin(set_a, set_b).all()

print("Is set_a a subset of set_b? ", is_subset(set_a, set_b))
"""