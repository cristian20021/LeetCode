class Solution(object):
    def findWordsContaining(self, words, x):
        lst = []
        for i in range(len(words)):
            if x in words[i]:
                lst.append(i)

        return lst