from data import A_matrix, b_vector, target_function
from cutoff_constraint import generate_cutoff_constraint_or_optimal_plan


def main() -> None:
    response = generate_cutoff_constraint_or_optimal_plan(
        A_matrix,
        b_vector,
        target_function
    )


if __name__ == '__main__':
    main()
