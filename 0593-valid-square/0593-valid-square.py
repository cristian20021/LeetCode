class Solution(object):
    def dist (self,x,y):
        print(sqrt(((x[0]-y[0])**2) + ((x[1]-y[1])**2)))
        return sqrt(((x[0]-y[0])**2) + ((x[1]-y[1])**2))

    def validSquare(self, p1, p2, p3, p4):
        if p1==p2==p3==p4:
            return False
        ls = [self.dist(p1,p2),self.dist(p1,p3),self.dist(p1,p4),self.dist(p2,p3),self.dist(p2,p4),self.dist(p3,p4)]
        ls.sort()
        if ls[0]==ls[1]==ls[2]==ls[3]:
            if ls[4]==ls[5]:
                return True
        return False