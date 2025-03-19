#! C:\Users\chrst\OneDrive\Documents\GitHub\NumPySymPy-Assignment\myenv\Scripts\python.exe

#SET THEORY
#SUBSETS
import numpy as np

set_a = {1,3,5,}
set_b = {2, 1, 4, 3, 6, 5}

def is_subset(set_a, set_b): 
    array_a = np.array(list(set_a))
    array_b = np.array(list(set_b))

    result = np.isin(array_a, array_b).all()
    return result

print("Is set_a a subset of set_b? ", is_subset(set_a, set_b))


#POWER SETS
from sympy import FiniteSet

def powerset(s):
    s = FiniteSet(*s)
    result = []

    for subset in s.powerset():
        result.append(subset)

    return sorted(result)

s = {1, 2, 3}
print(powerset(s))


#CARTESIAN PRODUCTS
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





#FUNCTIONS
#TYPES OF FUNCTIONS
import numpy as np

def is_one_to_one(f, domain):
    values = [f(x) for x in domain]
    return len(values) == len(set(values))

def is_onto(f, domain, codomain):
    values = set([f(x) for x in domain])
    return values.issuperset(codomain)

def function_type(f, domain, codomain):
    one_to_one = is_one_to_one(f, domain)
    onto = is_onto(f, domain, codomain)
    
    if one_to_one and onto:
        return 
    elif one_to_one:
        return 
    elif onto:
        return 
    else:
        return 

f = lambda x: x**2
domain = np.arange(-10, 11)
codomain = np.arange(0, 101)

print(function_type(f, domain, codomain))


#COMPOSITION OF FUNCTIONS
import sympy as sp

x = sp.symbols('x')
f = x**2
g = 2*x + 3

composition = f.subs(x, g)

print("Composition f(g(x)):", composition)

print("Simplified composition:", sp.simplify(composition))


#INVERSE FUNCTIONS
import sympy as sp

x, y = sp.symbols('x y')

f = 2*x + 3

f_inv = sp.solve(sp.Eq(y, f), x)

f_inv = f_inv[0].subs(y, x)

print("Inverse function f^(-1)(x):", f_inv)

composition = f.subs(x, f_inv)
print("Verification f(f^(-1)(x)):", sp.simplify(composition))





#RELATIONS
#PROPERTIES OF RELATIONS
import numpy as np

def is_reflexive(relation, set_A):
    return all((a, a) in relation for a in set_A)

def is_symmetric(relation):
    return all((b, a) in relation for (a, b) in relation)

def is_transitive(relation):
    for (a, b) in relation:
        for (c, d) in relation:
            if b == c and (a, d) not in relation:
                return False
    return True

set_A = {1, 2, 3}
relation = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (2, 3), (1, 3)}

print("Reflexive:", is_reflexive(relation, set_A))
print("Symmetric:", is_symmetric(relation))
print("Transitive:", is_transitive(relation))


#EQUIVALENCE OF RELATIONS
def is_equivalence_relation(relation, set_A):
    return (is_reflexive(relation, set_A) and
            is_symmetric(relation) and
            is_transitive(relation))

set_A = {1, 2, 3}
relation = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}

print("Equivalence Relation:", is_equivalence_relation(relation, set_A))


#PARTIAL ORDERINGS
def is_antisymmetric(relation):
    for (a, b) in relation:
        if (b, a) in relation and a != b:
            return False
    return True

def is_partial_ordering(relation, set_A):
    return (is_reflexive(relation, set_A) and
            is_antisymmetric(relation) and
            is_transitive(relation))

set_A = {1, 2, 3}
relation = {(1, 1), (2, 2), (3, 3), (1, 2), (1, 3)}

print("Partial Ordering:", is_partial_ordering(relation, set_A))

#HASSE DIAGRAM
import matplotlib.pyplot as plt
import networkx as nx

def draw_hasse_diagram(relation, set_A):
    G = nx.DiGraph()
    G.add_nodes_from(set_A)
    
    for (a, b) in relation:
        if a != b:  
            G.add_edge(a, b)
    
    for a in set_A:
        for b in set_A:
            if a != b and G.has_edge(a, b):
                for c in set_A:
                    if G.has_edge(b, c) and G.has_edge(a, c):
                        G.remove_edge(a, c)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=12, font_weight='bold', arrows=True)
    plt.show()

set_A = {1, 2, 3}
relation = {(1, 1), (2, 2), (3, 3), (1, 2), (1, 3)}

draw_hasse_diagram(relation, set_A)





#USING NUMPY AND SYMPY FOR SET, FUNCTION, AND RELATION OPERATIONS
#SET OPERATIONS
import numpy as np

def set_union(set1, set2):
    return np.union1d(set1, set2)

def set_intersection(set1, set2):
    return np.intersect1d(set1, set2)

def set_difference(set1, set2):
    return np.setdiff1d(set1, set2)

def set_complement(universal_set, set1):
    return np.setdiff1d(universal_set, set1)

set_A = np.array([1, 2, 3, 4])
set_B = np.array([3, 4, 5, 6])
universal_set = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print("Union:", set_union(set_A, set_B))
print("Intersection:", set_intersection(set_A, set_B))
print("Difference (A - B):", set_difference(set_A, set_B))
print("Complement of A:", set_complement(universal_set, set_A))

set_C = np.array([2, 4, 6, 8])
set_D = np.array([1, 3, 5, 7])
print("Union:", set_union(set_C, set_D))
print("Intersection:", set_intersection(set_C, set_D))
print("Difference (C - D):", set_difference(set_C, set_D))
print("Complement of C:", set_complement(universal_set, set_C))

set_E = np.array([1, 3, 5, 7])
set_F = np.array([2, 4, 6, 8])
print("Union:", set_union(set_E, set_F))
print("Intersection:", set_intersection(set_E, set_F))
print("Difference (E - F):", set_difference(set_E, set_F))
print("Complement of E:", set_complement(universal_set, set_E))





#FUNCTION OPERATIONS
import sympy as sp

x = sp.symbols('x')

f = x**2 + 3*x + 2

f_diff = sp.diff(f, x)
print("Derivative of f:", f_diff)

f_int = sp.integrate(f, x)
print("Integral of f:", f_int)

f_limit = sp.limit(f, x, 2)
print("Limit of f as x approaches 2:", f_limit)

g = sp.sin(x) + sp.cos(x)
print("Derivative of g:", sp.diff(g, x))
print("Integral of g:", sp.integrate(g, x))
print("Limit of g as x approaches 0:", sp.limit(g, x, 0))

h = sp.exp(x) * sp.log(x)
print("Derivative of h:", sp.diff(h, x))
print("Integral of h:", sp.integrate(h, x))
print("Limit of h as x approaches 1:", sp.limit(h, x, 1))

k = 1 / (1 + x**2)
print("Derivative of k:", sp.diff(k, x))
print("Integral of k:", sp.integrate(k, x))
print("Limit of k as x approaches infinity:", sp.limit(k, x, sp.oo))




#RELATION OPERATIONS
import numpy as np

def isReflexive(matrix):
    n = matrix.shape[0]
    return np.all(np.diag(matrix) == 1)

def isSymmetric(matrix):
    return np.all(matrix == matrix.T)

def isTransitive(matrix):
    n = matrix.shape[0]
    for i in range(n):
        for j in range(n):
            if matrix[i, j] == 1:
                for k in range(n):
                    if matrix[j, k] == 1 and matrix[i, k] != 1:
                        return False
    return True

relation_matrix = np.array([
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1]
])

print("Reflexive:", isReflexive(relation_matrix))
print("Symmetric:", isSymmetric(relation_matrix))
print("Transitive:", isTransitive(relation_matrix))

relation_matrix_1 = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])
print("Reflexive:", isReflexive(relation_matrix_1))
print("Symmetric:", isSymmetric(relation_matrix_1))
print("Transitive:", isTransitive(relation_matrix_1))

relation_matrix_2 = np.array([
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
])
print("Reflexive:", isReflexive(relation_matrix_2))
print("Symmetric:", isSymmetric(relation_matrix_2))
print("Transitive:", isTransitive(relation_matrix_2))

relation_matrix_3 = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])
print("Reflexive:", isReflexive(relation_matrix_3))
print("Symmetric:", isSymmetric(relation_matrix_3))
print("Transitive:", isTransitive(relation_matrix_3))