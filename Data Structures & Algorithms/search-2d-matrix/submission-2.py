class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] < target:
                continue
            l, r = 0, len(row)-1
            while l <= r:
                m = l + (r-l)//2

                if target > row[m]:
                    l = m+1
                elif target < row[m]:
                    r = m-1
                else:
                    return True
        return False