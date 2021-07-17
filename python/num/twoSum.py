#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.

def twoSum(nums, target):
    for i,num1 in enumerate(nums):
        res = target - num1
        for j,num2 in enumerate(nums):
            if num2 == res and i != j:
                return [i,j]

def better_twoSum(nums, target):
    h = {}
    for i, num in enumerate(nums):
        res = target - num
        if res not in h:
            h[num] = i
        else:
            return [h[res], i]

nums1 = [1,9]
target1 = 10

num2 = [0,0,2,3,4,5]
target2 = 9

num3 = [5,9,1,2,5]
target3 = 10

print(better_twoSum(nums1, target1))
print(better_twoSum(num2, target2))
print(better_twoSum(num3, target3))