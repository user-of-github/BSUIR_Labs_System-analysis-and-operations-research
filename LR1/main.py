from data import MATRIX_A_INITIAL, VECTOR_C, VECTOR_B, VECTOR_D_PLUS, VECTOR_D_MINUS
from branch_and_bound_method import get_solution_with_branch_and_bound_method


def main() -> None:
    solution = get_solution_with_branch_and_bound_method(
        MATRIX_A_INITIAL,
        VECTOR_C,
        VECTOR_B,
        VECTOR_D_MINUS,
        VECTOR_D_PLUS
    )

    print(solution)


if __name__ == '__main__':
    main()
