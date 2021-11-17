words_str = input()

words_str = words_str.strip('[]')
words = words_str.replace('"', '').replace('\'', '').split(',')

print(words)

# # 1st solution
# rows = [{'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'},
#         {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'},
#         {'z', 'x', 'c', 'v', 'b', 'n', 'm'}]

# result = []
# n_row = 0
# for word in words:
#     if len(word) == 1:
#         result.append(word)
#         continue

#     f = word[0].lower()
#     for i, row in enumerate(rows):
#         if f in row:
#             n_row = i
#             break
            
#     # if all(c in rows[n_row] for c in word.lower()):
#     #     result.append(word)

#     flag = 0
#     for index in range(1, len(word)):
#         if word[index].lower() not in rows[n_row]:
#             flag = 1
#             break
    
#     if flag == 0:
#         result.append(word)

# print(result)


# 2nd solution:
first_row = {'q','w','e','r','t','y','u','i','o','p'}
second_row = {'a','s','d','f','g','h','j','k','l'}
third_row = {'z','x','c','v','b','n','m'}

result = []
for word in words:
    if set(word.lower()) - first_row == set():
        result.append(word)
    elif set(word.lower()) - second_row == set():
        result.append(word)
    elif set(word.lower()) - third_row == set():
        result.append(word)

print(result)
