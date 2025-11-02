class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        seen = set()
        blocks = set()
        
        for i in guards:
            blocks.add((i[0], i[1]))
        for i in walls:
            blocks.add((i[0], i[1]))
        
        direc = [(0,1), (0,-1), (1,0), (-1,0)]
        
        for i in guards:
            r, c = i
            for d in direc:
                x = r + d[0]
                y = c + d[1]
                while 0 <= x < m and 0 <= y < n and (x, y) not in blocks:
                    seen.add((x, y))
                    x = x + d[0]
                    y = y + d[1]
        
        return m * n - len(seen) - len(blocks)