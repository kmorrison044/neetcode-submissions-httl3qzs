class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0 
        j = len(heights) - 1

        max_area = float("-inf")
        while (i < j):
            lim = min(heights[i], heights[j])
            area = lim * (j-i)
            if area > max_area:
                max_area = area
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return max_area