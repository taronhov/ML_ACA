# Knight’s Possible Moves (8, in total): {+/-2; +/-1} and {+/-1; +/-2}
px = int(input("Input initial x coordinate (px): "))
py = int(input("Input initial y coordinate (py): "))

# Knight's all 8 possible moves:
# X = [2, 2, -2, -2, 1, 1, -1, -1]
# Y = [1, -1, -1, 1, 2, -2, -2, 2]

X = [1, 2, 2, 1, -1, -2, -2, -1]
Y = [2, 1, -1, -2, -2, -1, 1, 2]

print(f"\nPossible final (x, y) coordinates are: ")
for i in range(8) :
    x = px + X[i]
    y = py + Y[i]
    print(x, y)