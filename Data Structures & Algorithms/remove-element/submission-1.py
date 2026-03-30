class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ind = []

        for i, n in enumerate(nums):
            if n != val:
                ind.append(n)
        
        for i in range(len(ind)):
            nums[i] = ind[i]

        for _ in range(len(nums) - len(ind)):
            nums.pop()

        return len(nums)
