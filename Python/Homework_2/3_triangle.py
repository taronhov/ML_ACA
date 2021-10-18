print("Enter the triangle sides (integers): ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if c < (a + b) and b < (a + c) and a < (b + c):
    # c² = a² + b² : the triangle is a right-angled triangle.
    # c² < a² + b² : the triangle is an acute-angle triangle.
    # c² > a² + b² : the triangle is an obtuse-angle triangle.

    a_cube = pow(a, 2)
    b_cube = pow(b, 2)
    c_cube = pow(c, 2)

    if (c_cube == (a_cube + b_cube) or b_cube == (a_cube + c_cube) or a_cube == (b_cube + c_cube)):
        print("\nRight Triangle\n")
    elif (a_cube > (b_cube + c_cube) or b_cube > (a_cube + c_cube) or c_cube > (a_cube + b_cube)):
        print("\nObtuse Triangle\n")
    else:
        print("\nAcute Triangle\n")

    if a == b == c:
    	print("Equilateral Triangle\n")
    elif a == b or b == c or c == a:
    	print("Isosceles Triangle\n")
    else:
    	print("Scalene Triangle\n")

else:
    print("\nNot a Triangle\n")
