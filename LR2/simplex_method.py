import numpy as np
from copy import deepcopy


def simplex_method(c, A, x, B):
    # STEP 1
    len_b = len(B)
    Ab = np.zeros((len_b, len_b))
    for i in range(len_b):
        Ab[:, i] = A[:, B[i]]

    Ab_inv = np.linalg.inv(Ab)

    while True:
        # STEP 2
        cb = np.zeros(len_b)
        for i in range(len_b):
            cb[i] = c[B[i]]

        # STEP 3
        u = np.dot(cb, Ab_inv)

        # STEP 4
        delta = np.dot(u, A) - c

        # STEP 5 and 6
        j0 = -1

        for i in range(len(delta)):
            if i in B:
                continue
            if delta[i] < 0:
                j0 = i
                break
        if j0 == -1:
            return x, B

        # STEP 7
        z = np.dot(Ab_inv, A[:, j0])

        # STEP 8
        theta = np.zeros(len_b)
        for i in range(len_b):
            if z[i] > 0:
                theta[i] = x[B[i]] / z[i]
            else:
                theta[i] = np.inf

        # STEP 9
        theta0 = min(theta)

        # STEP 10
        if theta0 == np.inf:
            return "The objective function is not bounded from above on the set of admissible plans"

        # STEP 11
        k, = np.where(np.isclose(theta, theta0))
        k = k[0]
        j_star = B[k]

        # STEP 12
        B[k] = j0

        # STEP 13
        for i in range(len(x)):
            if i == j0:
                x[j0] = theta0
            elif i in B:
                x[i] = x[i] - theta0 * z[B.index(i)]
            else:
                x[i] = 0

        x_ = A[:, j0]
        i_ = B.index(j0)
        Ab_inv = invert_matrix(Ab_inv, x_, i_)
        if isinstance(Ab_inv, str):
            return "Can't find a solution"
        Ab[:, i_] = x_

def check_for_reversibility(matrix_a_inv, matrix_x, i_for_check):
    l = np.dot(matrix_a_inv, matrix_x)
    return (False, l) if l[i_for_check] == 0 else (True, l)


def invert_matrix(a_inv_matrix, x, i_for_replace):
    matrix_order = len(a_inv_matrix)

    check, l_matrix = check_for_reversibility(a_inv_matrix, x, i_for_replace)
    if check:
        l_new = deepcopy(l_matrix)
        l_new[i_for_replace] = -1
        l_step_three = -1/l_matrix[i_for_replace] * l_new
        q_matrix = np.eye(matrix_order)
        for i in range(matrix_order):
            q_matrix[i][i_for_replace] = l_step_three[i]

        new_a_inv = np.dot(q_matrix, a_inv_matrix)
        return new_a_inv
    else:
        return "Can't find a solution"
