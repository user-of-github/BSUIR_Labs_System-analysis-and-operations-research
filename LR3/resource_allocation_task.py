def get_solution_of_resource_allocation_task(P: int, Q: int, A: list[list[int]]) -> list[int]:
    B: list[list[int]] = [[0] * (Q + 1) for _ in range(0, P, 1)]
    C: list[list[int]] = [[0] * (Q + 1) for _ in range(0, P, 1)]

    # direct way of method
    for p in range(0, P, 1):
        for q in range(0, Q + 1, 1):
            if p == 0:
                B[p][q] = A[p][q]
                C[p][q] = q
            else:
                temp: list[int] = [A[p][i] + B[p - 1][q - i] for i in range(0, q + 1, 1)]
                max_element: int = max(temp)
                max_element_index: int = temp.index(max_element)

                B[p][q] = max_element
                C[p][q] = max_element_index
                ops(C=C)

    # reversal way of method
    q: int = Q - 1
    p: int = P - 1

    print(B)
    print(C)

    agents: list[int] = [0] * P

    while p >= 0:
        agents[p] = C[p][q]
        p -= 1
        q -= C[p][q]

    return agents












def ops(C) -> None:
    C[0][0] = 2