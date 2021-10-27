
n = int(input("Enter the base width of the tree(an odd number): "))


str1 = "*"
str2 = " "

if (n % 2 != 0) and (n > 0):
    for i in range((n//2), -1, -1):
        print(i*str2, (n - (2*i))*str1, i*str2)
else:
    print("Error: enter an odd number greater, than '0'!")
