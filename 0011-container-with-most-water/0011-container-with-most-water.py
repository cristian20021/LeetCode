class Solution(object):
    def maxArea(self, height):
        left =  0
        right = len(height)-1
        maxi = 0
        while left < right:
            a = min(height[left],height[right])
            b = right-left
            maxi = max(maxi,a*b)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxi