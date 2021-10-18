n = int(input("Enter a natural number N: "))


def sum_of_digits(number):
    total_sum = 0

    while number > 0:
        total_sum += (number % 10)
        number //= 10

    if total_sum < 10:
        return total_sum
    else:
        print(total_sum)
        return sum_of_digits(total_sum)

print(n)
print(sum_of_digits(n))
