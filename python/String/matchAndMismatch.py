#Given two sentences, return an array that has the words that appear in one sentence and not
#the other and an array with the words in common.
# use set() to initialize a set not {}
# {} is for empty dict
# ^ A.symmetric_difference(B), & A.intersection(B) | A.union(B)   - A.different(B)


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
    def match_mismatch(self,str1,str2):
        sentence1 = set(str1.split())
        sentence2 = set(str2.split())
        return list(sentence1 & sentence2),list(sentence1^sentence2)

sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'

test = Sulotion()
print(test.match_and_mismatch(sentence1,sentence2))
print(test.match_mismatch(sentence1,sentence2))