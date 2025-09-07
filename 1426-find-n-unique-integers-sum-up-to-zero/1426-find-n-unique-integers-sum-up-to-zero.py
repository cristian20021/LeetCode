class Solution(object):
    
    def sumZero(self, n):
        outOdd = [0]
        outEven = []
        if n%2 == 0:

            for i in range(1,(n/2)+1):
              
                outEven.append(i)
                outEven.append(-abs(i))
                

            return outEven
        else:

            for i in range(1,(n/2)+1):
        
             
                outOdd.append(i)
                outOdd.append(-abs(i))

            return outOdd

        