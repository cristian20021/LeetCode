class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        final = 0
        for i in operations:
            if '+' in i:
                final+=1
            else:
                final-=1
        return final