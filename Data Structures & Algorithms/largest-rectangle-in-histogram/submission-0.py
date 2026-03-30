class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0

        for i in range(len(heights)):
            minimum = float("inf")
            for j in range(i, len(heights)):
                minimum = min(minimum, heights[j])
                area = min(minimum, heights[j]) * (j - i + 1)
                print(area)
                max_area = max(area, max_area)
        
        return max_area
