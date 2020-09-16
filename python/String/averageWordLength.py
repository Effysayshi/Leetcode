class Solution:
    def averange_word_length(self, sentence):
        for p in "!?',;.":
            sentence = sentence.replace(p, '')
        words = sentence.split()
        print (round(sum(len(word) for word in words) / len(words), 2))

def run_test():
    sentence1 = "Hi all, my name is Tom...I am originally from Australia."
    sentence2 = "I need to work very hard to learn more about algorithms in Python!"
    test1 = Solution()
    test2 = Solution()
    test1.averange_word_length(sentence1)
    test2.averange_word_length(sentence2)

run_test()