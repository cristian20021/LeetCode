class Solution(object):
    def canThreePartsEqualSum(self, arr):
        total = sum(arr)
        if total % 3 != 0:
            return False
        target = total // 3
        count = 0
        curr_sum = 0
        for i in range(len(arr)): 
            curr_sum += arr[i]  
            if curr_sum == target:
                count += 1
                curr_sum = 0
            if count == 2 and i < len(arr) - 1:
                return True
        return False