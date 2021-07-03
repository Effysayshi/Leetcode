class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookUpDict = {}
        for i,num1 in enumerate(nums):
            if num1 in lookUpDict and i!= lookUpDict[num1]:
                return [lookUpDict[nums[i]], i]
            else:
                lookUpDict[target - num1] = i
                
