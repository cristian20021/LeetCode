class Solution(object):
    def largestTriangleArea(self, points):
        maxx = 0
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                for z in range(j+1,len(points)):
                    if 0.5*abs(points[i][0]*(points[j][1]-points[z][1])+points[j][0]*(points[z][1]-points[i][1]) + points[z][0]*(points[i][1]-points[j][1]))>maxx:
                        maxx = 0.5*abs(points[i][0]*(points[j][1]-points[z][1])+points[j][0]*(points[z][1]-points[i][1]) + points[z][0]*(points[i][1]-points[j][1]))
        return maxx