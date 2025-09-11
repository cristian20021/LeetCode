class Solution(object):
    def sortVowels(self, s):
        vow = ['a','e','i','o','u','A','E','I','O','U']
        local_vow = []
        newS = ''
        count = 0

        for i in s:
            if i in vow:
                local_vow.append(i)
        local_vow = sorted(local_vow)

        for j in range(len(s)):
            if s[j] not in vow:
                newS+=s[j]
            else:
                newS+=local_vow[count]
                count+=1
                
        return newS