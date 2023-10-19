import numpy as np
from copy import deepcopy
from simplex_method import simplex_method


def generate_cutoff_constraint_or_optimal_plan(a_matrix: np.array, b_vector: np.array, target_functional: np.array) -> np.array:
    A: np.array = deepcopy(a_matrix)
    b: np.array = deepcopy(b_vector)
    c: np.array = deepcopy(target_functional)

    m: int = len(c)
    n: int = len(b)

    # STEP 1
    x = np.hstack((np.zeros(m - n), b))
    B = [i for i in range(m - n, m)]

    x_with_roof, B = simplex_method(c, A, x, B)

    # print(f"x = {x_with_roof}")
    # print(f"B = {B}")

    # STEP 2
    k = -1
    j0 = -1
    for i in range(len(x_with_roof)):
        if not float(x[i]) == int(x[i]):
            j0 = i
            k = B.index(i)
            break
    else:
        print(f"Optimal plan x = {x_with_roof}")

    N: list[int] = [i for i in range(m) if i not in B]
    # print(f"j = {j0}")
    # print(f"k = {k}")
    # print(f"N = {N}")

    # STEP 3
    # print("\nSTEP 3:")
    A_b = np.zeros((n, n))

    for i in range(n):
        A_b[:, i] = A[:, B[i]]

    # print("Ab:")
    # print(A_b)

    len_n = len(N)
    A_n = np.zeros((len_n, len_n))

    for i in range(len_n):
        A_n[:, i] = A[:, N[i]]

    # print("An:")
    # print(A_n)

    # STEP 4
    # print("\nSTEP 4:")
    Ab_inv = np.linalg.inv(A_b)
    # print("A(b^-1):")
    # print(Ab_inv)

    # STEP 5
    # print("\nSTEP 5:")
    Ab_inv_dot_An = np.dot(Ab_inv, A_n)
    # print("Matrix product:")
    # print(Ab_inv_dot_An)

    # STEP 6
    # print("\nSTEP 6:")
    l = Ab_inv_dot_An[k]
    # print(f"l = {l}")
    l_fractional_parts = [l[i] - np.floor(l[i]) for i in range(len(l))]

    print("Cutoff Constraints:")
    print(f"{l_fractional_parts[0]} x_{N[0] + 1} ", end='')

    for i in range(1, len(l_fractional_parts)):
        print(f"+ {l_fractional_parts[i]} x_{N[i] + 1}", end=" ")

    print(f"- x_{m + 1} = {x_with_roof[j0] - np.floor(x_with_roof[j0])}")
