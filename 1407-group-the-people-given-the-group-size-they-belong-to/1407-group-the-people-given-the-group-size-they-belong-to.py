class Solution(object):
    def check(self,amount,groupSizes):
        localArr = []
        count = 0
        j = 0
        while count<amount:
            if groupSizes[j] == amount:
                localArr.append(j)
                groupSizes[j] = -1
                count+=1
            j+=1
        if len(localArr) != 0:
            return localArr


    def groupThePeople(self, groupSizes):
        fin = []
        for i in range(len(groupSizes)):
            loc = self.check(groupSizes[i],groupSizes)
            try:
                if len(loc)>0:
                    fin.append(loc)
            except:
                pass

        return fin