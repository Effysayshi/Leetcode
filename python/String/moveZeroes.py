#Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of
#the non-zero elements.
class Solution:
    def move_zeroes(self,array):
        for i in array:
            if i == 0:
                array.remove(i)
                array.append(0)
        return array

array1 = [1,0,2,0,3,0]
array2 = [0,2,3,3,0,0]

test = Solution()
print(test.move_zeroes(array1))
print(test.move_zeroes(array2))

#use while 0 in array to remove all the zeroes
#but do not use it to move zeroes!infinitely loop warning

def remove_zeroes(array):
    while 0 in array:
        array.remove(0)
    return array