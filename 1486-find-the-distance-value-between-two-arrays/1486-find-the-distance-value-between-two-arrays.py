class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        count = 0
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])<=d:
                    count-=1
                    break
            count+=1
        return count