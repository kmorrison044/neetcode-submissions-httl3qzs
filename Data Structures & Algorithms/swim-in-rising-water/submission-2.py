class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = [[False] * n for _ in range(n)]
        minH = maxH = grid[0][0]
        for row in range(n):
            maxH = max(maxH, max(grid[row]))
            minH = min(minH, min(grid[row]))

        def dfs(node, t):
            r, c = node
            if (min(r, c) < 0 or max(r, c) >= n or
                visit[r][c] or grid[r][c] > t):
                return False
            if r == (n - 1) and c == (n - 1):
                return True
            visit[r][c] = True
            return (dfs((r + 1, c), t) or
                    dfs((r - 1, c), t) or
                    dfs((r, c + 1), t) or
                    dfs((r, c - 1), t))

        for t in range(minH, maxH):
            if dfs((0, 0), t):
                return t
            for r in range(n):
                for c in range(n):
                    visit[r][c] = False

        return maxH
# class Solution:
#     def swimInWater(self, grid: List[List[int]]) -> int:
#         row, col = len(grid), len(grid[0])

#         def dfs(i, j, t):
#             if i == row - 1 and j == col - 1:
#                 return t
#             if i >= row or j >= col or i < 0 or j < 0:
#                 return float('inf')
            
#             t_1 = t_2 = t_3 = float('inf')
#             if i + 1 < row and grid[i + 1][j] <= t:
#                 t_1 = dfs(i + 1, j, t)
#             if j + 1 < col and grid[i][j + 1] <= t:
#                 t_2 = dfs(i, j + 1, t)

#             if t_1 == float('inf') and t_2 == float('inf'):
#                 return dfs(i, j, t + 1)
            
#             return min(t_1, t_2)

#         return dfs(0, 0, 0)