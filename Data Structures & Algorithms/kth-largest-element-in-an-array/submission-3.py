class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for n in nums:
            if len(q) < k:
                heapq.heappush(q, n)
            else:
                heapq.heappushpop(q, n)
                
        return q[0]