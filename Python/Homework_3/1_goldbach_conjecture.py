
def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False 
    return True


def goldbach(num):
    if num <= 2:
        return f"Error '{num}' is not greater than 2: Goldbach Conjecture is true only for even numbers greater than 2!"
    elif (num % 2) != 0:
        return f"Error '{num}' is not an even number " 
    else:
        # "We need to process it...
        # Can be optimized by excluding non-prime numbers from the following loop (using known facts about primes)...
        for i in range(2, num):
            if is_prime(i) == True:
                for j in range(i, num):
                    if is_prime(j) == True and (num == (i + j)):
                        # return f"{num} = {i} + {j}"
                        return f"{i} {j}"


num = int(input("Enter an even natural number (N <= 10000): "))

print(goldbach(num))
