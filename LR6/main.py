from tsp import tsp_algorithm
from data import cities, distances




def main() -> None:
    min_tour = tsp_algorithm(cities, distances)
    print(f'Минимальная длина маршрута: {min_tour}')


if __name__ == '__main__':
    main()
