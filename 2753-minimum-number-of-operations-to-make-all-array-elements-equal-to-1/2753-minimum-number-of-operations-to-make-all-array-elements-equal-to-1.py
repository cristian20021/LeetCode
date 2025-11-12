class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        ones_count = nums.count(1)
        if ones_count > 0:
            return n - ones_count
        
        min_k = float('inf')
        
        for i in range(n):
            current_g = nums[i]
            for j in range(i + 1, n):
                current_g = self.gcd(current_g, nums[j])
                if current_g == 1:
                    k = (j - i) + 1
                    min_k = min(min_k, k)
                    break
        
        if min_k == float('inf'):
            return -1
            
        ops_to_create_one = min_k - 1
        ops_to_spread = n - 1
        
        return ops_to_create_one + ops_to_spread