class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        new_word = ''
        for i in words:
            new_word+=i[0]
        return new_word == s