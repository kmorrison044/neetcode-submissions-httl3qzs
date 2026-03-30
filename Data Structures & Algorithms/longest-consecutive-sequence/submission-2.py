class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        longest = 0

        for num in nums:
            if num-1 not in hset:
                curr_len = 1
                while num+1 in hset:
                    curr_len += 1
                    num += 1
                longest = max(longest, curr_len)

        return longest
