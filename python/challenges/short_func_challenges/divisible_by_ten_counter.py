def divisible_by_ten(nums):
    count = 0
    for i in nums:
        if i % 10 == 0:
            count += 1
    return count

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))