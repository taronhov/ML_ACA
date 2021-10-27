
print("Enter N and k numbers and a sequence of whole numbers of length N: ")
n = int(input("Enter N: "))
k_in = int(input("Enter k: "))
sequence_in  = input("Enter the sequence: ")

sequence_float = list(map(float, sequence_in.strip().split(" ")))

if n != len(sequence_float):
    print("N has a wrong value!!!")
    n = len(sequence_float)


sequence_out = []

# 1. Find the number of real/actual shifts: k % N (0, if k == N)
k = k_in % n

# 2. Perform the cyclic shift (k times) by copying the array/list into a new array/list
for i in range(0, n):
    if i < k:
        sequence_out.append(sequence_float[i + (n - k)])
    else:
        sequence_out.append(sequence_float[i - k])

print(sequence_out)