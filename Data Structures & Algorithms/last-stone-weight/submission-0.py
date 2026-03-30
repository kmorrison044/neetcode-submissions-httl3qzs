class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = [-stone for stone in stones]
        heapq.heapify(q)

        while len(q) > 1:
            x = heapq.heappop(q)
            y = heapq.heappop(q)

            new_weight = min(x, y) - max(x, y)
            if new_weight:
                heapq.heappush(q, new_weight)
        
        return -q[0] if q else 0