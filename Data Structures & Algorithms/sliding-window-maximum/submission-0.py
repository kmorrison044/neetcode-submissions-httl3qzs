class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # To solve this problem, a queue should be used because we want to
        # efficiently pop from the right and left of the data structure.

        output = []
        q = deque()
        l = r = 0

        while r < len(nums):
            # If the current value in the array is greater than the rightmost
            # value in the queue, that means we can remove elements in the queue
            # from consideration of the current maximum or future maximums.
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # Appending indices
            q.append(r)

            # Remove elements outside the window
            if l > q[0]:
                q.popleft()

            # Once the window is set, append the leftmost value in the queue
            # to the output array, which represents the maximum in the current
            # window, then increment your l pointer
            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        
        return output
