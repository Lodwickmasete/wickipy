import re

def simplify_to_linear(equation):
    # Remove spaces
    equation = equation.replace(" ", "")

    # Validate the equation
    if "=" not in equation:
        return "Invalid equation format. An equation must have '='."

    # Split into left and right sides
    left, right = equation.split("=")
    steps = [f"Given equation: {equation}"]

    # Parse terms from both sides
    def parse_terms(expression):
        terms = re.findall(r"[+-]?\d*x|[+-]?\d+", expression)
        coefficient_x = 0
        constant = 0
        for term in terms:
            if 'x' in term:  # Coefficient of x
                coeff = term.replace('x', '')
                coeff = int(coeff) if coeff not in ["", "+", "-"] else (1 if coeff in ["", "+"] else -1)
                coefficient_x += coeff
            else:  # Constant term
                constant += int(term)
        return coefficient_x, constant

    left_coeff_x, left_constant = parse_terms(left)
    right_coeff_x, right_constant = parse_terms(right)

    steps.append("Step 1: Parse terms from both sides of the equation.")
    steps.append(f"Left side: {left_coeff_x}x + {left_constant}")
    steps.append(f"Right side: {right_coeff_x}x + {right_constant}")

    # Combine terms: move all x terms to the left and constants to the right
    combined_coeff_x = left_coeff_x - right_coeff_x
    combined_constant = right_constant - left_constant

    steps.append("Step 2: Move all x terms to one side and constants to the other side.")
    steps.append(f"Resulting equation: {combined_coeff_x}x + ({combined_constant}) = 0")

    # Check for contradictions or special cases
    if combined_coeff_x == 0 and combined_constant != 0:
        steps.append("Step 3: The equation reduces to a contradiction.")
        steps.append(f"{combined_constant} = 0 is not true. No solution exists.")
        return "\n".join(steps)

    if combined_coeff_x == 0 and combined_constant == 0:
        steps.append("Step 3: The equation is valid for all values of x.")
        steps.append("Infinitely many solutions exist.")
        return "\n".join(steps)

    # Build the simplified equation
    simplified = ""
    if combined_coeff_x != 0:
        simplified += f"{'' if combined_coeff_x == 1 else '-' if combined_coeff_x == -1 else combined_coeff_x}x"
    if combined_constant != 0:
        if combined_constant > 0:
            simplified += f"+{combined_constant}"
        else:
            simplified += f"{combined_constant}"
    simplified += "=0"

    steps.append("Step 3: Simplify the equation to standard linear form.")
    steps.append(f"Simplified equation: {simplified}")

    return "\n".join(steps), simplified
    
    """
# Example equations to simplify
equations = [
    "2x - 2 = 4x - 4",
    "2x = 3x - 3",
    "2x - 3x = -1",
    "x + x = 2x + x",
    "x + x + x = x + x - 1",
    "x + x = x",
    "x + x = x + x",
    "x - 2 = x - 3"
]

for eq in equations:
    simplified = simplify_to_linear(eq)
    print(f"Original: {eq}")
    print(f"Simplified: {simplified}")
    if "Invalid" not in simplified:
        print(simplified)

    print("-" * 40)
    """