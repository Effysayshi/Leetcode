 ## A set is an unordered collection with no duplicate elements. Using set to return the result without duplicate elements.
 ## create an empty set use set()
 ## the average time complexity of looking up a dictionary(or a map) is O(1)
 ## Tuple can be added to a set,but list cannot.(list is unhashable and immutable)
 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lookUpDict = {} 
        res = set()
        
        for i in range(len(nums)):
            lookUpDict[nums[i]] = i
            
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                num = - (nums[i] + nums[j])
                if num in lookUpDict and lookUpDict[num] > j:
                        res.add((nums[i], nums[j], num))
        
        return res;
