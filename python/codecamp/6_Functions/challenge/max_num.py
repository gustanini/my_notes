def max_num(nums):
    max = nums[0]
    for i in nums:
        if i > max:
            max = i
    return max