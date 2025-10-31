class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dupl = []
        track = []
        for i in nums:
            if i in track:
                dupl.append(i)
            else:
                track.append(i)
        return dupl