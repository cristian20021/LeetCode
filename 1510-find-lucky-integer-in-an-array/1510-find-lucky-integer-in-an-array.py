class Solution(object):
    def findLucky(self, arr):
        dictLuck = {}
        for i in arr:
            if i not in dictLuck:
                dictLuck[i] = 1
            else:
                dictLuck[i] += 1
        maxx = 0
        for k , v in dictLuck.items():
            if k == v:
                maxx = k
        if maxx>0:
            return maxx
        return -1