import re

def solve_linear_equation(equation):
    # Remove spaces
    equation = equation.replace(" ", "")
    
    # Handle direct equations like "x = 4"
    if "=" in equation and equation.count("=") == 1 and "x" in equation:
        left, right = equation.split("=")
        if re.fullmatch(r"[+-]?\d*x?", left) and re.fullmatch(r"[+-]?\d*", right):
            left_coeff = int(left.replace("x", "") or "1")
            right_value = int(right or "0")
            if left_coeff == 0:
                return "Invalid equation: no solution exists."
            x = right_value / left_coeff
            return f"Given equation: {equation}\nStep 1: Solve directly.\nx = {x}"
    
    # Validate format
    if "=" not in equation or not equation.endswith("=0"):
        return "Invalid equation format. Use the format 'ax + b = 0'."
    
    # Normalize the equation (split at '=0')
    equation = equation.split("=0")[0]
    
    # Parse terms
    terms = re.findall(r"[+-]?\d*x|[+-]?\d+", equation)
    coefficient_x = 0
    constant = 0
    combine_step_needed = False

    for term in terms:
        if 'x' in term:  # Coefficient of x
            coeff = term.replace('x', '')
            coeff = int(coeff) if coeff not in ["", "+", "-"] else (1 if coeff in ["", "+"] else -1)
            if coefficient_x != 0:
                combine_step_needed = True
            coefficient_x += coeff
        else:  # Constant
            if constant != 0:
                combine_step_needed = True
            constant += int(term)

    # Handle cases based on coefficients
    if coefficient_x == 0:
        if constant == 0:
            return "The equation is valid for all values of x (infinitely many solutions)."
        else:
            return "No solution exists for the equation because it reduces to a contradiction."

    # Steps for solving
    steps = []
    steps.append(f"Given equation: {equation} = 0")
    if combine_step_needed:
        steps.append(f"Step 1: Combine like terms.")
        combined = f"{'' if coefficient_x == 1 else coefficient_x}x"
        if constant != 0:
            combined += f" + ({constant})"
        steps.append(f"{combined} = 0")
    else:
        steps.append(f"Step 1: Simplify the equation.\n{equation} = 0")

    # Check if constant is already 0
    if constant != 0:
        steps.append(f"Step 2: Move the constant term to the other side.")
        steps.append(f"{'' if coefficient_x == 1 else coefficient_x}x = {-constant}")
    
    # Step 3: Solve for x
    if coefficient_x == 1:
        x = -constant
        steps.append(f"Step 3: Solve for x.\nx = {x}")
    else:
        x = -constant / coefficient_x
        if x.is_integer():
            x = int(x)
        steps.append(f"Step 3: Solve for x.\nx = {-constant}/{coefficient_x}\nx = {x}")

    return "\n".join(steps)
"""
# Example usage
equations = [
    "2x + x = 0",
    "44x + 37x + 5 = 0",
    "-7 + x + 3 = 0",
    "3x + 4 + 4x = 0",
    "x + x + x + x - 10 = 0",
    "0x + 0 = 0",
    "x + 3 = 0",
    "5x = 0",
    "x = 5"
]

for eq in equations:
    print(f"Solving: {eq}")
    print(solve_linear_equation(eq))
    print("-" * 40)
"""