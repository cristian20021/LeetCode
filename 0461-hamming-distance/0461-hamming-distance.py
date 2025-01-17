class Solution(object):
    def hammingDistance(self, x, y):
        x_b = str(format(x ,"0512b"))
        y_b = str(format(y ,"0512b"))
        count = 0
        for i in range(len(x_b)):
            if x_b[i]!=y_b[i]:
                count+=1
        return count
        