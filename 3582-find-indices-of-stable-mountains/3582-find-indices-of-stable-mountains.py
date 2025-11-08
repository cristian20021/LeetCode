class Solution(object):
    def stableMountains(self, height, threshold):
        """
        :type height: List[int]
        :type threshold: int
        :rtype: List[int]
        """
        stable_mount = []
        for i in range(1,len(height)):
            if height[i-1]>threshold:
                stable_mount.append(i)
        return stable_mount