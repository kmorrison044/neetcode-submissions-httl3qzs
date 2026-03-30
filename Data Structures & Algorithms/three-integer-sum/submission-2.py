class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        for i in range(len(nums)):
            j = i+1
            k = len(nums) - 1
            while j < k:
                check = [nums[i], nums[j], nums[k]]
                three_sum = sum(check)
                if three_sum > 0:
                    k -= 1
                elif three_sum < 0:
                    j += 1
                else:
                    if not any(set(sub) == set(check) for sub in ret):
                        ret.append(check)
                    j += 1
                    k -= 1

        return ret