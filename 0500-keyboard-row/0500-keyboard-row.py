class Solution(object):
    def check(self,i,coll):
        
        for j in i:
            if j.lower() not in coll:
                return False
        return True

    def findWords(self, words):
   
        lst = []
        for i in words:
            if i[0].lower() in 'qwertyuiop':
                if self.check(i,'qwertyuiop') == True:
                    lst.append(i)
                

            elif i[0].lower() in "asdfghjkl":
                if self.check(i,'asdfghjkl') == True:
                    lst.append(i)
                                
            else:
                if self.check(i,'zxcvbnm') == True:
                    lst.append(i)
        return lst