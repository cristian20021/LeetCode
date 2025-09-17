class Solution(object):
    def judgeSquareSum(self, c):
        a = 0
        b = int(sqrt(c))

        while a<=b:
            if a*a + b*b == c:
                return True
            elif a*a + b*b > c:
                b-=1
            else:
                a+=1
                
        return False