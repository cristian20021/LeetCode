class Solution:
    def pacificAtlantic(self, heights):
        if not heights: return []
        m, n = len(heights), len(heights[0])
        pac = [[False]*n for _ in range(m)]
        atl = [[False]*n for _ in range(m)]
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(i, j, vis):
            vis[i][j] = True
            for dx, dy in dirs:
                x, y = i+dx, j+dy
                if 0 <= x < m and 0 <= y < n and not vis[x][y] and heights[x][y] >= heights[i][j]:
                    dfs(x, y, vis)

        for i in range(m):
            dfs(i, 0, pac)
            dfs(i, n-1, atl)
        for j in range(n):
            dfs(0, j, pac)
            dfs(m-1, j, atl)

        return [[i, j] for i in range(m) for j in range(n) if pac[i][j] and atl[i][j]]