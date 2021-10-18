n = int(input("Enter a natural number: "))

product = (1 if n > 0 else 0)

while n > 0:
    remainder = (n % 10)
    if remainder > 0:
        product *= remainder

    n //= 10

print(product)