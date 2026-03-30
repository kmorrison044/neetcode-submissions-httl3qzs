class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        ret = []
        pac, atl = set(), set()

        def dfs(r, c, visit):
            if (r, c) in visit:
                return

            visit.add((r, c))
            curr = heights[r][c]
            if r + 1 < ROWS and heights[r+1][c] >= curr: dfs(r + 1, c, visit)
            if r - 1 >= 0 and heights[r-1][c] >= curr: dfs(r - 1, c, visit)
            if c + 1 < COLS and heights[r][c+1] >= curr: dfs(r, c + 1, visit)
            if c - 1 >= 0 and heights[r][c-1] >= curr: dfs(r, c - 1, visit)

        for r in range(ROWS):
            dfs(r, 0, pac)
            dfs(r, COLS - 1, atl)

        for c in range(COLS):
            dfs(0, c, pac)
            dfs(ROWS - 1, c, atl)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    ret.append([r, c])
        
        return ret