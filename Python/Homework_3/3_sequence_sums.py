
sequence = input("Enter a sequence of real numbers (A): ")

# sequence_int = [float(x) for x in sequence.strip().split(" ")]
sequence_float = list(map(float, sequence.strip().split(" ")))


sequence_out = []

sum_all = 0

# i-th element of the sequence B is equal to the sum of all elements in sequence A starting from i-th
for i in range((len(sequence_float) - 1), -1, -1):
    sum_all += sequence_float[i]
    sequence_out.append(sum_all)

sequence_out.reverse()
print(sequence_out)
