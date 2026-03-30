class Solution:
    def findMin(self, nums: List[int]) -> int:
       l, r = 0, len(nums)-1

       while l <= r:
            m = l + (r-l) // 2

            if (m == 0 and nums[m] <= nums[-1]) or (nums[m-1] > nums[m]):
                return nums[m]
            elif nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1
