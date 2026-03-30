class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # This solution does not gaurentee order nor does it actually remove the unwanted elements.
        # It simply just ensures that the first "k" elements do not equal val.
        # This allows the algo to be done in O(n) space as well.
        i = 0
        n = len(nums)
        while i < n:
            # If we meet the unwanted val, take a num from the end of the list and replace
            # the current element. DO NOT increment "i" as we are not gaurenteed to replace
            # it with a value not equal to val. Just decrement n.
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            # If above is false, increment i
            else:
                i += 1
        return n