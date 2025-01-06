`simplify.py`
Example equations to simplify
```
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

```
