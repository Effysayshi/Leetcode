class Solution:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)):
            j = len(s) - i - 1
            if (i < j):
                s[i], s[j] = s[j], s[i]
        print(s)


def run_test():
    test = Solution()
    test.reverseString(['h','e','l','l','o'])
    print(5/2)

run_test()