# Given an array containing None values fill in the None values with most recent
# non None value in the array
class Solution:
    def fill_blanks(self,str):
        newStr = []
        start = 0
        while str[start] is None:
            start += 1
        valid = str[start]
        for i in str:
            if i is not None:
                newStr.append(i)
                valid = i
            else:
                newStr.append(valid)
        return newStr

array1 = [1,None,2,3,None,None,5,None]
array2 = [None,1,2,3,None]
test = Solution()
print(test.fill_blanks(array1))