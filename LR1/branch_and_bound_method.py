import numpy as np
import math
from copy import deepcopy
from dual_simplex import dual_simplex_method


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

    alpha: float = 0

    # step 3
    # declare type for stored items in stack
    LinearProgrammingIssueItem = tuple[np.array, np.array, np.array, np.array, np.array, float]
    stack: list[LinearProgrammingIssueItem] = []

    x_star: list[float] = []
    record: float = -np.inf

    stack.append((c, a, b, d_minus, d_minus, alpha))

    iterations_count: int = 0

    # step 4: iterations
    while stack:
        iterations_count += 1
        current_c, current_a, current_b, current_d_minus, current_delta, current_alpha = stack.pop()
        alpha_new = current_alpha + np.dot(current_c, current_d_minus)
        b: np.array = current_b - np.dot(current_a, current_d_minus)
        B: list[int] = [n + i for i in range(n + m)]
        x_wave: np.array = dual_simplex_method(current_c, current_a, b, B)

        if x_wave is None:
            continue

        is_plan_fully_integer: bool = all(list(map(lambda x: x == int(x), x_wave)))

        if is_plan_fully_integer:
            x_lid = np.array(x_wave) + current_delta
            record_current: float = np.dot(current_c, x_lid) + alpha_new

            if len(x_star) == 0 or record < record_current:
                x_star = deepcopy(x_lid)
                record = record_current
        else:
            first_float: int = -1

            for index in range(0, len(x_wave), 1):
                if int(x_wave[index]) != x_wave[index]:
                    first_float = index
                    break

            record_current: float = math.floor(np.dot(current_c, x_wave) + alpha_new)

            if len(x_star) == 0 or record < record_current:
                b_new_new: np.array = np.copy(b)
                b_new_new[m + first_float] = math.floor(x_wave[first_float])
                d_minus_new: np.array = np.zeros(2 * n + m)
                d_minus_new[first_float] = math.ceil(x_wave[first_float])
                new_delta: np.array = current_delta + d_minus_new

                stack.append((current_c, current_a, b_new_new, np.zeros(2 * n + m), current_delta, alpha_new))
                stack.append((current_c, current_a, b, d_minus_new, new_delta, alpha_new))

    if len(x_star) == 0:
        print('Not solvable')
        return None

    for i in range(n):
        if vector_c[i] >= 0:
            x_star[i] *= -1

    return x_star[:n]
