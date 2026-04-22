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
            temp = set()
            num = nums[i]
            for t in dp:
                temp.add(num + t)
                temp.add(t)

                if target in temp:
                    return True
            dp = temp
        
        return False