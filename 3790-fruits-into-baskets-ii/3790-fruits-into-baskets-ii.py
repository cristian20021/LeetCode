class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if fruits[i]<=baskets[j]:
                    baskets[j] = -1
                    break
        count = 0
        for b in baskets:
            if b is not -1:
                count+=1
        return count