class Solution(object):

    def minOperations(self, boxes):
        newL = []
        for i in range(len(boxes)):
            count = 0
            for j in range(len(boxes)):
                if boxes[j]=='1':
                    count+= abs(j-i)
            newL.append(count)
        return newL