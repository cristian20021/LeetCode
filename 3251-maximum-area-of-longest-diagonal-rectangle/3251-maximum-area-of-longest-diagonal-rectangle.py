
class Solution(object):
    import math
    def areaOfMaxDiagonal(self, dimensions):
        area = 0
        diag = 0
        for i in range(len(dimensions)):
            if math.sqrt(dimensions[i][0]**2 + dimensions[i][1]**2)>diag:
                diag = math.sqrt(dimensions[i][0]**2 + dimensions[i][1]**2)
                area = dimensions[i][0] * dimensions[i][1]
            elif math.sqrt(dimensions[i][0]**2 + dimensions[i][1]**2) == diag:
                if dimensions[i][0] * dimensions[i][1] > area:
                    area = dimensions[i][0] * dimensions[i][1]
        return area