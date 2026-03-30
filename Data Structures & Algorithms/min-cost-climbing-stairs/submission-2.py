class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # Start from the 3rd to last element in the array, and
        # Add the cost of the current jump with the minimum of the
        # costs of taking one step vs two steps. Iterate backwards and add
        # those costs, changing the costs to the original array.
        for i in range(n - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        
        # Since you can start at index 0 or 1, return the minimum of the
        # values of the first two indices.
        return min(cost[0], cost[1])
