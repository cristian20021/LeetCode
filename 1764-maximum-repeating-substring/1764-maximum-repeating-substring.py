class Solution(object):
    def maxRepeating(self, sequence, word):
        count = 0
        while word * (count + 1) in sequence:
            count +=  1        
        return count