class Solution(object):
    def lemonadeChange(self, bills):
        if bills[0]!=5:
            return False
        
        ten_dollar = 0
        five_dollar = 0

        for i in bills:
            if i == 5:
                five_dollar+=1
            elif i ==10:
                if five_dollar>0:
                    five_dollar-=1
                else:
                    return False
                ten_dollar+=1
            else:
                if five_dollar>0 and ten_dollar>0:
                        ten_dollar -=1
                        five_dollar -=1
                elif five_dollar>2:
                    five_dollar-=3
                else:
                    return False
        return True
        