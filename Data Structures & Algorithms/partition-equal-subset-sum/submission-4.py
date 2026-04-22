class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False
        
        n = len(nums)
        target = total // 2
        dp = set()
        # We could always have 0 in our set of subproblem targets, since we could
        # choose to not select any number. This is the base case.
        dp.add(0)

        # Bottom up approach
        for i in range(n - 1, -1, -1):
            # Create a temp set to add to so we are not changing the dp set
            # in the middle of the loop.
            temp = set()
            num = nums[i]

            # Iterate over every subproblem target in dp, add the current number + each target
            # number in dp as well as the target number itself to temp (to account
            # for all of the subproblem targets already in dp), then check if the target is 
            # in temp. If it is, then return True.
            for t in dp:
                temp.add(num + t)
                temp.add(t)

                if target in temp:
                    return True
            
            # Set dp to the added subproblem targets in temp
            dp = temp
        
        # If we couldn't find any matching subproblem targets == overall target,
        # return false
        return False