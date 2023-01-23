def over_nine_thousand(nums):
    sum = 0
    for i in nums:
        sum += i
        if sum >= 9000:
            break
        else:
            continue
    return sum