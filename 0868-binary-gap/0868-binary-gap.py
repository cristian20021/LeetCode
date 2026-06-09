class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary_n = str(bin(n)[2:])
        print(binary_n)
        if n < 5 and n!= 3:
            return 0
        if n == 3:
            return 1
        maxx = 0
        first_index = 0
        second_index = 1

       
        while second_index<len(binary_n):
            if binary_n[second_index] == '1':
                if second_index - first_index  > maxx:
                    maxx = second_index - first_index 
                    
                first_index = second_index
                second_index += 1
            else:
                second_index+=1
        return maxx 
        