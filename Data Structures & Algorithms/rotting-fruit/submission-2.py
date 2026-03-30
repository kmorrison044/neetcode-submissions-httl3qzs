class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        rot = False
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in dirs:
                    row = r + dr
                    col = c + dc

                    if (0 <= row < ROWS and 0 <= col < COLS and
                        grid[row][col] == 1):
                        rot = True
                        grid[row][col] = 2
                        q.append((row, col))
            print(grid)
            if rot:
                rot = False
                time += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    q.append((r, c))
        
        if len(q) != 0:
            return -1

        return time