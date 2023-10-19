from data import P, Q, A
from resource_allocation_task import get_solution_of_resource_allocation_task


def main() -> None:
    solution = get_solution_of_resource_allocation_task(P, Q, A)
    print(solution)


if __name__ == '__main__':
    main()
