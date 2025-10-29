class Solution(object):
    def check(self,n):
        n_str = str(n)
        for i in n_str:
            if i == "0":
                return False
        return True

    def smallestNumber(self, n):
        while True:
            if self.check(format(n ,"b")) == True:
                return n
                break
            else:
                n+=1