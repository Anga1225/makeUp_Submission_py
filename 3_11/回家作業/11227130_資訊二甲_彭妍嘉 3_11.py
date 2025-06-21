import math
a = 1
b = -3
c = 2
print(f"Quadratic equation: {a}x² + {b}x + {c} = 0")
print()
discriminant = b ** 2 - 4 * a * c
print(f"Discriminant = b² - 4ac = {b}² - 4({a})({c}) = {discriminant}")
if discriminant > 0:
    # Two real solutions
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Two real solutions:")
    print(f"x₁ = {x1}")
    print(f"x₂ = {x2}")
elif discriminant == 0:
    # One real solution
    x = -b / (2 * a)
    print(f"One real solution:")
    print(f"x = {x}")
else:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-discriminant) / (2 * a)
    print(f"Two complex solutions:")
    print(f"x₁ = {real_part} + {imaginary_part}i")
    print(f"x₂ = {real_part} - {imaginary_part}i")

print(f"4ac = 4 × {a} × {c} = {4 * a * c}")
print(f"b² = {b}² = {b ** 2}")