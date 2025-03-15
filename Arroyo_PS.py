
# Function to generate power set
def power_set(s):
    if not s:
        return [[]]
    first = s[0]
    rest = power_set(s[1:])
    return rest + [[first] + subset for subset in rest]

# Input set
input_set = [1, 2, 3]

# Generate the power set
result = power_set(input_set)

# Print the result
print("Power set:", result)

# Verify with SymPy
from sympy import FiniteSet, powerset

input_set_sympy = FiniteSet(1, 2, 3)
sympy_power_set = [list(subset) for subset in powerset(input_set_sympy)]

print("SymPy power set:", sympy_power_set)

if result == sympy_power_set:
    print("The results match!")
else:
    print("The results do not match.")

"""
import numpy as np

set_a = {1,3,5}
set_b = {2, 1, 4, 3, 6, 5}

def is_subset(set_a, set_b): 
    array_a = np.array(list(set_a))
    array_b = np.array(list(set_b))

    result = np.isin(array_a, array_b).all()
    return result

print("Is set_a a subset of set_b? ", is_subset(set_a, set_b))
"""