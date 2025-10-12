class Solution(object):
    from itertools import permutations

    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        
        perm = permutations(digits,3)
        count  = 0
        fin = []
        for i in perm:
            if i[0] != 0 and i not in fin and i[-1]%2 == 0:
                count+=1
                fin.append(i)
        return count