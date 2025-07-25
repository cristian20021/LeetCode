class Solution(object):
    def countSymmetricIntegers(self, low, high):
        count = 0
        for i in range(low,high+1):
            if (i>9 and i<100) or (i>999 and i<10000):
                n = int(len(str(i)) / 2)
                localLstInt = [int(x) for x in str(i)]
                if sum(localLstInt[:n]) == sum(localLstInt[n:]):        
                    count+=1
        return count