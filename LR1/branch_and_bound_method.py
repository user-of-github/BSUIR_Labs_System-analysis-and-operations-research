import numpy as np
from copy import deepcopy


def get_solution_with_branch_and_bound_method(
        matrix_a: np.array,
        vector_c: np.array,
        vector_b: np.array,
        vector_d_minus: np.array,
        vector_d_plus: np.array
) -> np.array:
    # just copy items to work
    c: np.array = deepcopy(vector_c)
    a: np.array = deepcopy(matrix_a)
    b: np.array = deepcopy(vector_b)
    d_minus: np.array = deepcopy(vector_d_minus)
    d_plus: np.array = deepcopy(vector_d_plus)
    n: int = len(c)
    m: int = len(a[0])

    # step 1
    for index in range(0, n, 1):
        if c[index] > 0:
            c[index] *= -1

            for row in range(0, n, 1):
                a[row][index] *= -1

            d_plus[index] *= -1
            d_minus[index] *= -1

            (d_plus[index], d_minus[index]) = (d_minus[index], d_plus[index])

    # step 2
    matrix_from_below = np.identity(n)
    matrix_from_right = np.identity(m + n)

    a = np.concatenate((a, matrix_from_below))
    a = np.concatenate((a, matrix_from_right), axis=1)

    b = np.concatenate((b, d_plus))
    d_minus = np.concatenate((d_minus, np.array([0] * (n + m))))
    c = np.concatenate((c, np.array([0] * (n + m))))

    print(a)
    print(b)
    print(c)
    print(d_minus)

    # step 3
    # declare type for stored items in stack
    LinearProgrammingIssueItem = tuple[np.array, np.array, np.array]
    stack: list[LinearProgrammingIssueItem] = []




    return np.array([])



