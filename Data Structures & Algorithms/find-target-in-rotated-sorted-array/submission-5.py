class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r-l) // 2
            curr = nums[m]

            if curr == target:
                return m

            if nums[l] <= curr:
                if target > curr or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < curr or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            
        return -1