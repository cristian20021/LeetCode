
def is_ascending(lst):
        ''' determine if the given list of ints is in strict ascending order'''

        return all(a<b for a,b in zip(lst, lst[1:]))
class Solution(object):
    

    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for i in range(len(nums)-(k*2)+1):
            if is_ascending(nums[i:k+i])  and is_ascending(nums[i+k:i+k+k]) :
                return True
        return False