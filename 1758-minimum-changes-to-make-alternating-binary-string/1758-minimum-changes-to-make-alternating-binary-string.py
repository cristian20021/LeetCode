class Solution(object):

            
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        count1 = 0
        first = '0'
        second = '1'
        for i in range(0,len(s),2):
            if s[i] != first:
                count1+=1
        for j in range(1,len(s),2):
            if s[j] != second:
                count1+=1

        first = '1'
        second = '0'
        count2 = 0
        for i in range(0,len(s),2):
            if s[i] != first:
                count2+=1
        for j in range(1,len(s),2):
            if s[j] != second:
                count2+=1
 
        if count1>count2:
            return count2
        return count1