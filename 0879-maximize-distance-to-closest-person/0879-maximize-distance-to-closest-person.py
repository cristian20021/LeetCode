class Solution(object):
    def maxDistToClosest(self, seats):
        maxx = 0
        j = 1
        i = 0
        
        while j<=len(seats)-1:
            if seats[j]==1:
                if seats[i] == 1:
                  localMax = (j-i)/2
                else:
                    localMax = j
                if localMax>maxx:
                    maxx=localMax
                i = j
                j += 1
            else:
                j+=1  

        if maxx == 0:
            return j-1

        elif seats[-1] == 0:
            if len(seats)-i-1>maxx:
                return len(seats)-i-1

        return maxx
