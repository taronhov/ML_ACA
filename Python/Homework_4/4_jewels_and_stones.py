jewels = input("jewels = ")
stones = input("stones = ")

jewels_count = 0

for char in stones:
    if char in jewels:
        jewels_count += 1

print(jewels_count)
