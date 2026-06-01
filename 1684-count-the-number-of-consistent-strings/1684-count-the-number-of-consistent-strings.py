class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for i in words:
            passi = True
            for letter in i:
                if letter not in allowed:
                    passi = False
                    break
            if passi == True:
                count+=1
        
        return count