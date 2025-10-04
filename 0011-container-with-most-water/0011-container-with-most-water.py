class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        maxx = 0
        while left<right:
            h = min(height[left],height[right])
            dist = right - left
            maxx = max(maxx,h*dist)
            if height[right]>height[left]:
                left+=1
            else:
                right-=1

        return maxx