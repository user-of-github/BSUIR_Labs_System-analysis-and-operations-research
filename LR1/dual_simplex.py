import numpy as np


def dual_simplex_method(c, A, b, B) -> np.array:
    while True:
        len_b = len(B)
        A_b = np.zeros((len_b, len_b))
        for i in range(len_b):
            A_b[:, i] = A[:, B[i]]

        A_b_inv = np.linalg.inv(A_b)

        c_b = [c[i] for i in B]

        y = np.dot(c_b, A_b_inv)
        k = np.zeros(len(c))
        A_b_inv_b = np.dot(A_b_inv, b)
        for i in range(len(B)):
            k[B[i]] = A_b_inv_b[i]
        jk = -1
        is_optimal_plan = True

        for el in k:
            if el < 0:
                jk = el
                is_optimal_plan = False
                break

        if is_optimal_plan:
            return k

        k0 = list(k).index(jk)
        delta_y = A_b[B.index(k0)]

        not_B = list(set(range(len(c))) - set(B))
        mu = np.zeros(len(not_B))
        for j in range(len(mu)):
            mu[j] = np.dot(delta_y, A[:, not_B[j]])

        neg_mu = list()
        for elem in mu:
            if elem < 0:
                neg_mu.append(not_B[list(mu).index(elem)])
        if not neg_mu:
            return None

        sigmas = np.zeros(len(neg_mu))
        for j in range(len(sigmas)):
            i = neg_mu[j]
            sigmas[j] = (c[i] - np.dot(A[:, i], y)) / mu[j]

        sigma0 = min(sigmas)
        j0 = list(sigmas).index(sigma0)

        B[B.index(k0)] = not_B[j0]