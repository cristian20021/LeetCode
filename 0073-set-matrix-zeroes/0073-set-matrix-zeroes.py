class Solution(object):

    def setZeroes(self, matrix):
        locations = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    locations.append([i,j])
        for z in locations:
            for a in range(len(matrix[z[0]])):
                matrix[z[0]][a] = 0
        for x in locations:
            for s in range(len(matrix)):
                matrix[s][x[1]] = 0

                    