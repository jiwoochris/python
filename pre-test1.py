def FindBalance(nums):
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i+1:]):
            index = i
            value = nums[index]
            weight = sum(nums[:index])

    return [index, value, weight]


print(FindBalance([1,2,3,4,5,2,3,5]))