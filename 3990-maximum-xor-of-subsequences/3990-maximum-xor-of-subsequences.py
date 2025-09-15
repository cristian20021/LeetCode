class Solution(object):
    def maxXorSubsequences(self, nums):


        basis = [0] * 31

        for x in nums:
            v = x
            for b in range(30, -1, -1):
                if not (v & (1 << b)):
                    continue
                if basis[b]:
                    v ^= basis[b]
                else:
                    basis[b] = v
                    break

        res = 0
        for b in range(30, -1, -1):
            res = max(res, res ^ basis[b])

        return res
        