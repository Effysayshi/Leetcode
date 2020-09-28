#Given two sentences, return an array that has the words that appear in one sentence and not
#the other and an array with the words in common.


class Sulotion:
    def match_and_mismatch(self,str1,str2):
        array1,array2 = str1.split(),str2.split()
        words = {}
        match = []
        mismatch = []
        for i in array1:
            words[i] = 1
        for j in array2:
            if j in words:
                words[j] = 2
            else:
                words[j] = 1
        for word in words:
            if words[word] == 2:
                match.append(word)
            else:
                mismatch.append(word)
        return match,mismatch

sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'

test = Sulotion()
print(test.match_and_mismatch(sentence1,sentence2))