from sympy import FiniteSet

def powerset(s):
    s = FiniteSet(*s)
    result = []

    for subset in s.powerset():
        result.append(subset)

    return sorted(result)

s = {1, 2, 3}
print(powerset(s))