class Solution(object):
    def successfulPairs(self, spells, potions, success):
        finalArr = []
        potions.sort()
        for i in range(len(spells)):
            low = 0
            high = len(potions) - 1
            while low<= high:
                mid = (low+high)//2
                if spells[i]*potions[mid] >=success:
                    high = mid - 1
                else:
                    low = mid + 1
            finalArr.append(len(potions)-low)
        return finalArr