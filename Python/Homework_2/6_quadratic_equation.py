import math

# The roots of a quadratic equation can be classified as: 
# 1. If b*b < 4*a*c, then roots are complex
# 2. If b*b == 4*a*c, then roots are real, and both roots are the same.
# 3. If b*b > 4*a*c, then roots are real and different
def quadr_equation_roots( a, b, c): 

    discriminant = (b * b) - (4 * a * c)
    sqrt_val = math.sqrt(abs(discriminant)) 
    x1 = 0
    x2 = 0

    print("Quadratic equation")
    print(f"Discriminant: {discriminant}")

    # Checking the discriminant:
    if discriminant > 0: 
        # Real and different roots
        x1 = (-b + sqrt_val) / (2 * a)
        x2 = (-b - sqrt_val) / (2 * a)
        print(f"Two solutions: ({x1}; {x2}) \n")

    elif discriminant == 0: 
        # Real roots, which are the same
        x1 = x2 = -b / (2 * a)
        print(f"One solution: {x1} \n")

    else:
        # If the discriminant is less than 0:
        print("No solutions")
        print("Complex Roots\n") 
        # print(f"{-b / (2 * a)} + i{sqrt_val}") 
        # print(f"{-b / (2 * a)} - i{sqrt_val}")




# Main code
print("Enter the factors of a quadratic equation (rational numbers): ")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

x = 0

if a == 0:
    # Non-quadratic
    if b == 0:
        if c == 0:
            print("Non-quadratic equation")
            print("Infinite solutions \n")
        else:
            print("Non-quadratic equation")
            print("No solutions \n")
    else:
        # A linear equation: bx + c = 0
        x = -c / b
        print("Non-quadratic equation")
        print(f"One solution: {x} \n")
else: 
    quadr_equation_roots(a, b, c)
