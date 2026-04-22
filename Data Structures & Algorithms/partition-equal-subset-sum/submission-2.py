class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False
        
        n = len(nums)
        target = total // 2
        dp = set()
        dp.add(0)

        for i in range(n - 1, -1, -1):
            if target in dp:
                return True

            temp = dp.copy()
            num = nums[i]
            for t in dp:
                temp.add(num + t)
            dp = temp
        
        return False