class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        newL = text.split()
        count = len(newL)
        for i in range(len(newL)):
            for j in newL[i]:
                if j in brokenLetters:
                    
                    count-=1
                    break

        return count