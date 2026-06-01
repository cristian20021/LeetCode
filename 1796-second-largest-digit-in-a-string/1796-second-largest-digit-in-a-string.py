class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        new_list = []
        for i in s:
          
            try:
                int_var = int(i)
                if int_var not in new_list:
                    
                    new_list.append(int_var)
            except:
                pass

        new_list.sort(reverse=True)

        if len(new_list)<2:
            return -1
        else:
            return new_list[1]