
# Given is a three-digit number on stdin
number_in = int(input("Enter a three-digit integer (positive) number: \n"))

digit_3 = number_in // 100
digit_2 = (number_in % 100) // 10
digit_1 = number_in % 10

# Print the sum of all 3 digits of the number
print("Here is the sum of all three digits: ")
print(digit_1 + digit_2 + digit_3)