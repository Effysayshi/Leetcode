# Given k numbers which are less than n, return the set of prime number among them
# Note: The task is to write a program to print all Prime numbers in an Interval.
# Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

class Solution:
    def prime_numbers_array(self,n):
        primeNums = []
        for i in range(2,n+1):
            flag = 1
            for j in range(2,i//2):
                if i % j == 0:
                    flag = 0
            if flag:
                primeNums.append(i)
        return primeNums
test = Solution()
print(test.prime_numbers_array(35))
print(test.prime_numbers_array(0))
print(test.prime_numbers_array(1))
print(test.prime_numbers_array(2))