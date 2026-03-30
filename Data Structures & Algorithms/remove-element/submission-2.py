class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # This solution modifies the list in place and keeps the order of elements
        # intact as well as removes the unwanted vals in the list in O(n) time.
        # Keeping them in order and actually removing the elements were not in
        # scope of the problem after rereading it.
        ind = []

        for i, n in enumerate(nums):
            if n != val:
                ind.append(n)
        
        for i in range(len(ind)):
            nums[i] = ind[i]

        for _ in range(len(nums) - len(ind)):
            nums.pop()

        return len(nums)
