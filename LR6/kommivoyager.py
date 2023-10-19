import itertools


def tsp_algorithm(cities, distances):
    n: int = len(cities)
    OPT: dict = dict()

    for i in range(1, n):
        OPT[(frozenset([cities[i]]), cities[i])] = distances[0][i]

    for k in range(3, n + 1):
        subsets = itertools.combinations(cities[1:], k - 1)

        for S in subsets:
            S = frozenset(S)

            for ci in S:
                OPT[(S, ci)] = float('inf')

                for cj in S:
                    if ci != cj:
                        OPT[(S, ci)] = min(OPT.get((S, ci), float('inf')), OPT.get((S - {ci}, cj), float('inf')) + distances[cities.index(cj)][cities.index(ci)])

    min_tour = float('inf')

    for ci in range(1, n):
        tour_length = OPT.get((frozenset(cities[1:]), cities[ci]), float('inf')) + distances[cities.index(ci)][0]
        min_tour = min(min_tour, tour_length)

    return min_tour
