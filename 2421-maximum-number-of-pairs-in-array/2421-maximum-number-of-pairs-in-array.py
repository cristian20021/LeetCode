class Solution(object):
    def numberOfPairs(self, nums):
        pairs = 0
        single = []

        for num in nums:
                    if num in single:
                        single.remove(num)
                        pairs += 1
                    else:
                        single.append(num)

        return [pairs, len(single)]
        