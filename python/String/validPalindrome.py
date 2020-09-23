class Solution:
    def valid_Palindrome(self,s):
        for i in range(len(s)):
            t = s[:i] + s[i + 1:]
            if t == t[::-1]: return True

        return s == s[::-1]

str1 = "aabb"
str2 = "abcdfcba"
str3 = "aaaac"
str4 = "true"


test = Solution()
print(test.valid_Palindrome(str1))
print(test.valid_Palindrome(str2))
print(test.valid_Palindrome(str3))
print(test.valid_Palindrome(str4))