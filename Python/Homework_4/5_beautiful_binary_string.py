str_len = int(input("Enter the length of the string: "))
bin_str = input("Enter the binary string: ")

bin_str = bin_str.strip()
if str_len != len(bin_str):
    print("Length of the string has a wrong value!!!")
    str_len = len(bin_str)

# count_010 = 0
# i = 0
# while i < (len(bin_str) - 1):
#     if bin_str[i:i+3] == "010":
#         count_010 += 1
#         i += 3
#     else:
#         i += 1

count_010 = bin_str.count("010")

print(count_010)