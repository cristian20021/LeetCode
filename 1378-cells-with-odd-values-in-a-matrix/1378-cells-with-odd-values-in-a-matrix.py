class Solution(object):
    def oddCells(self, m, n, indices):
        matrix = [[ 0 for j in range(1, n+1)] # 1
                             for i in range(m)]
        for x in indices:
            row = x[0]
            col = x[1]
            for f in range(len(matrix)):
                matrix[f][col]+=1 #col add

            for k in range(len(matrix[0])):
                matrix[row][k]+=1
        odd_nums = 0
        for inn in range(len(matrix)):
            for jnn in range(len(matrix[inn])):
                    if matrix[inn][jnn] % 2 != 0:
                        odd_nums+=1
        return odd_nums
        
        