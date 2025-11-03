class Solution(object):
    def minn(self,arr):
        maxx = max(arr)
        localArr = arr[:]
        localArr.remove(maxx)
        return sum(localArr)

    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        if len(colors) == 1:
            return 0

        total_time = 0
        start = 0
        currLetter = colors[0]
        for i in range(1,len(colors)):
            if colors[i]==currLetter:
                pass
            else:
                if i+1-start == 1:
                    pass
                else:
                    total_time+= self.minn(neededTime[start:i])
                    start = i
                    currLetter = colors[i]

                    #total_time += min(neededTime[i],neededTime[i+1])
        if i+1 - start > 1:
            total_time+= self.minn(neededTime[start:i+1])
        return total_time
