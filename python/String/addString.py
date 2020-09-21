#function eval() calculate the string
#function ord(num) - ord('0') convert char to int
class Solution:
    def add_string_1(self,num1,num2):
        print(eval(num1) + eval(num2))

    def convert_str_to_num(self,nums):
        sum = 0
        for i,num in enumerate(nums):
            sum += int(num) * (10**(len(nums) - i -1))
        return sum

    def add_string_2(self,num1,num2):
        print(self.convert_str_to_num(num1) + self.convert_str_to_num(num2))


num1 = "364"
num2 = "1836"

test1 = Solution()
test1.add_string_1(num1,num2)

test2 = Solution()
test2.add_string_2(num1,num2)