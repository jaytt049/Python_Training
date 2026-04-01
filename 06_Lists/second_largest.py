nums = [1, 2, 3, 4, 5]

max = nums[0]
second_max = nums[0]

for num in nums:
    if num>max:
        second_max = max
        max = num

print(f"second max number : {second_max}")

