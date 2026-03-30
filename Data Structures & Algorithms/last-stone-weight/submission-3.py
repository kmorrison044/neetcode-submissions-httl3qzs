class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Make the list a max heap (gotta use -1 on all values for max heap)
        q = [-stone for stone in stones]
        heapq.heapify(q)

        # Iterate while the q has more than 1 element
        while len(q) > 1:
            # Take the two largest values
            x = heapq.heappop(q)
            y = heapq.heappop(q)

            # Determine the new weight and if it is not 0, push to the heap
            new_weight = min(x, y) - max(x, y)
            if new_weight:
                heapq.heappush(q, new_weight)
        
        # Return the only element if there is one, else return 0
        return -q[0] if q else 0