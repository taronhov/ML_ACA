n = int(input("Enter a natural number N: "))

largest_power_of_3 = 1
curr_power = 1

while pow(3, curr_power) < n:
    largest_power_of_3 = curr_power
    curr_power += 1 
    # print(pow(3, curr_power))

print(pow(3, largest_power_of_3))
