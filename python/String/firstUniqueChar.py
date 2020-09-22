# Given a string, find the first non-repeating character in it and return its index.
# If it doesn't exist, return -1. # Note: all the input strings are already lowercase.
import collections
class Solution1:
    def fisrt_unique_character(self,str):
        dict = {}
        for char in str:
            if char not in dict.keys():
                dict[char] = 1
            else:
                dict[char] += 1
        for i in range(len(str)):
            if dict[str[i]] == 1:
                return i
        return -1

class Solution2:
    def first_unique_character(self,str):
        dict = collections.Counter(str)

        for i,char in enumerate(str):
            if dict[char] == 1:
                return i
        return -1

str1 = "alphabet"
str2 = "aabbcce"
str3 = "aabbcc"

test1 = Solution1()
print(test1.fisrt_unique_character(str1))
print(test1.fisrt_unique_character(str2))
print(test1.fisrt_unique_character(str3))

print("##")

test2 = Solution2()
print(test2.first_unique_character(str1))
print(test2.first_unique_character(str2))
print(test2.first_unique_character(str3))

