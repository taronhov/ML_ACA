# A solution to find all divisiors of a given number:

# div_count = 0

# # A simple/brute-force solution:
# for divisor in range(1, x+1):
#     if (x % divisor) == 0:
#         div_count += 1

# print(div_count)


# A better solution:
import math
 
# A function to print the divisors:
def get_all_divisors(n):
     
    # Note: this loop runs till square root!
    div_count = 0

    i = 1
    while i <= math.sqrt(n):
        if ((n % i) == 0):
            # If the divisors are equal, get only one:
            if ((n / i) == i):
                # print (i)
                div_count += 1
            # Otherwise, get both:
            else:
                # print (i, (n / i))
                div_count += 2
        i += 1
    
    return div_count


# Main code:
x = int(input("Enter a positive x (integer): "))

print (f"The total number of divisors of {x} is: ")
print(get_all_divisors(x))





