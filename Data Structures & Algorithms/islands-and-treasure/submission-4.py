class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2 ** 31 - 1
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        # Grab all treasure chests and add them to the deque
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        # Perform bfs loop to start from the treasure and go out.
        # Add one to each space from the previous space.
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF:
                        grid[nr][nc] = grid[r][c] + 1
                        q.append((nr, nc))