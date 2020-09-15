#Given a input string and reverse the vowels of the string
#vowels are 'aeiouAEIOU' not including 'y'
#use 2 pointer approach searching the vowels from left and right,
#important condition left < right!
class Solution:
    def reverseVowels(self, s: str) -> str:
        input = list(s)
        left,right = 0, len(input) - 1
        while left < right:
            if input[left] in 'AEIOUaeiou':
                if input[right] not in 'AEIOUaeiou':
                    right -= 1
                else:
                    input[left],input[right] = input[right],input[left]
                    left,right = left+1,right-1
            else:
                left += 1

        print(''.join(input))

test = Solution()
test.reverseVowels('hello')