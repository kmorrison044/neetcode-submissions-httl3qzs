class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        N = row * col
        res = []
        l, r = 0, col - 1
        top, bot = 0, row - 1

        while top <= bot and l <= r:
            # Right:
            for j in range(l, r + 1):
                res.append(matrix[top][j])
            top += 1
            
            # Down:
            for i in range(top, bot + 1):
                res.append(matrix[i][r])
            r -= 1
            
            # Left:
            if top <= bot:
                for j in range(r, l - 1, -1):
                    res.append(matrix[bot][j])
            bot -= 1
            
            # Up:
            if l <= r:
                for i in range(bot, top - 1, -1):
                    res.append(matrix[i][l])
            l += 1

        return res