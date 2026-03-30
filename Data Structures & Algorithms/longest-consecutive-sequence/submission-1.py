class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        dict_n = set(nums)
        for n in dict_n:
            current = 1
            if n-1 not in dict_n:
                while n + current in dict_n:
                    current += 1
            longest = max(current, longest)
        return longest
            