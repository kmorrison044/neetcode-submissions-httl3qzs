class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem_map = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in mem_map:
                return [mem_map[diff], i]
            
            mem_map[n] = i