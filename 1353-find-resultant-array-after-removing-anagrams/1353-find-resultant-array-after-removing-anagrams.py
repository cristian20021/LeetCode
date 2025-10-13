class Solution(object):
    def removeAnagrams(self, words):

        ans = [words[0]]
        for i in range(1,len(words)):
            a = sorted(words[i])
            b = sorted(words[i-1])
            if a!=b:
                ans.append(words[i])
        return ans