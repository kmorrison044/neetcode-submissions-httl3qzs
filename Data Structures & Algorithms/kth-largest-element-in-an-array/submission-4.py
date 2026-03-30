class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Instantiate a new list that will be a heap
        q = []
        # Iterate through all numbers
        for n in nums:
            # If the length of q is < k, then add the numbers to the heap,
            # this represents the largest numbers seen so far, with the 
            # smallest number at the front of the list
            if len(q) < k:
                heapq.heappush(q, n)
            # Otherwise, add the new element, and immediately remove the smallest
            else:
                heapq.heappushpop(q, n)

        # At the end, since we were constantly removing the smallest number,
        # The queue contains exactly the k largest numbers. The smallest of 
        # the largest numbers is the kth largest number.
        return q[0]