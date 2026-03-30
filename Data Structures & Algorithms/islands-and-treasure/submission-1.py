class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2 ** 31 - 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            q = deque([(r, c)])
            visit = [[False] * len(grid[r]) for _ in range(len(grid))]
            visit[r][c] = True
            
            steps = 0
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return steps

                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if (0 <= nr < len(grid) and 0 <= nc < len(grid[r]) and
                            not visit[nr][nc] and grid[nr][nc] != -1):
                            visit[nr][nc] = True
                            q.append((nr, nc))
                steps += 1
            return INF
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)