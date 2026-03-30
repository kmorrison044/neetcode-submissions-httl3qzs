class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        ret = []

        # Maintain two sets that tracks what cells can reach what oceans
        pac, atl = set(), set()

        # We are going to start dfs from the edges of the grid. That way we know
        # any cells it touches from there can reach that particular ocean.
        # "visit" param is the set of the ocean we are starting from.
        # The trick is that since we are starting from the edges of the grid,
        # we want to check if the next cells are "greater than" the value of the
        # current cell to ensure more inward cells can flow downward.
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
            # Start from left side and iterate all rows (i.e  pacific)
            dfs(r, 0, pac)
            # Start from right side and iterate all rows (i.e. atlantic)
            dfs(r, COLS - 1, atl)

        for c in range(COLS):
            # Start from top and iterate all cols (i.e  pacific)
            dfs(0, c, pac)
            # Start from bottom and iterate all cols (i.e. atlantic)
            dfs(ROWS - 1, c, atl)

        # Iterate across the entire board and check if that cell is
        # in both the pac and atl sets. If so append to ret.
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    ret.append([r, c])
        
        return ret