class Solution(object):
    def returnWord (self,word):
        alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        newWord = ''
        for j in range(len(word)):
            newWord+=word[j]
            newWord+=alph[alph.index(word[j])+1]
        return newWord
    def kthCharacter(self, k):
       
        word = 'a'
        for i in range(10):
            word = self.returnWord(word)
        print(word)
        return word[k-1]