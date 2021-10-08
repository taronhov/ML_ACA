# Arithmetic Progression: an = a1 + ((n - 1) * d)
print("Input the first two members (a1, a2) of an arithmetic progression and a n number (positive integers): ")
a1 = int(input("The 1-st (a1) member is: "))
a2 = int(input("The 2-nd (a2) member is: "))
n = int(input("n is: "))

d = (a2 - a1) 

an = a1 + ((n - 1 ) * d)

print("The n-th member of progression is: ")
print(an)