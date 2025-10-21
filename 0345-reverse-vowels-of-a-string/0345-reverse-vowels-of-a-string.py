class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s) 
        vowels = ['a', 'e', 'i', 'o', 'u']
        localVowels = []
        for i in s:
            if i.lower() in vowels:
                localVowels.append(i)

        localVowelsReversed = localVowels[::-1]
        count = 0

        for j in range(len(s)):
            if s[j].lower() in vowels:
                s[j]=localVowelsReversed[count]
                count+=1
        return "".join(s)