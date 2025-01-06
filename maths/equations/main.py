from simplify import simplify_to_linear
from solve import solve_linear_equation

def main():
    equations = [
        "2x - 2 = 4x - 4",
        "2x = 3x - 3",
        "2x - 3x = -1",
        "x + x = 2x + x",
        "x + x + x = x + x - 1",
        "x + x = x",
        "x + x = x + x",
        "x - 2 = x - 3",
        "1 = 3"
    ]

    for eq in equations:
        print(f"Original: {eq}")
        result = simplify_to_linear(eq)

        if isinstance(result, tuple):  # If the simplification succeeded
            steps, simplified = result
            print(steps)
            print("\nCalling solver on:", simplified)
            print(solve_linear_equation(simplified))
        else:  # If it failed or resulted in contradiction
            print(result)
        print("-" * 40)

if __name__ == "__main__":
    main()
