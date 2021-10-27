# Input 2 positive integer numbers a and b (а <= b): 
# We need to reverse the number and compare the number and the reverse...

def palindrome_check(num):

    orig_num = num
    rev_num = 0

    # Reversig the number
    while(num > 0):
        digit = num % 10
        # "Shifting" 1 position to left and appending new digit from right:
        rev_num = (rev_num * 10) + digit
        num //= 10

    if (rev_num == orig_num):
        # The number is a palindrome!
        return True
    else:
        # The number is not a palindrome!
        return False


print("Enter 2 positive integer numbers a and b (а <= b): ")
a = int(input("Enter a: "))
b = int(input("Enter b: "))

for num in range(a, b):
    if palindrome_check(num) == True:
        print(num)
