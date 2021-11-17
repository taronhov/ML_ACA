nums_str = input()

nums_str = nums_str.strip('[]')
nums = list(map(int, nums_str.split(',')))

out_nums = []


# 1st solution:
# n = len(nums)

# nums = set(nums)

# for index in range(1, n + 1):
#     if index not in nums:
#         out_nums.append(index)

# print(out_nums)


# 2nd solution:
for num in nums:
    real_num = abs(num)
    if nums[real_num - 1] > 0:
        nums[real_num - 1] *= -1
    # nums[real_num - 1] = abs(nums[real_num - 1]) * -1
        
out_nums = [(i + 1) for i in range(len(nums)) if (nums[i] > 0)]

print(out_nums)
