class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # DP Steps:
        # 1) Identify optimal substructure
        # 2) Write down the recurrence for the solution.
        # 3) Memoize the solution
        # 4) Recover the solution

        
        # We want to partition the array where the sum of each partition is equal.
        # This is to say that each partition should equal half of the sum of the original
        # array. Therefore, if the sum of the original array is odd, then you cannot
        # partition the array in such a way to make both partitions equal in sum.
        total = sum(nums)
        if total % 2:
            return False
        
        n = len(nums)
        target = total // 2

        # Because we are breaking the problem down into subproblems
        # by making a sequence of decisions, and based off the decision,
        # we are solving an instance of the original problem, and the final solution involves
        # solving the subproblems optmimally and combining with the original decision,
        # then this problem has an optimal substructure.

        # The -1 represents that we haven't visited this index/target combo yet. Create a memo
        # table for each possible index/target combination
        memo = [[-1] * (target + 1) for _ in range(n + 1)]

        def dfs(i, target):
            # If we successfully reduced the target down to 0 by taking numbers from the
            # array, then we found a partition equal to half of the sum of the subarray
            if target == 0:
                return True
            
            # If the index is greater than n or target is less than 0, then we haven't
            # found an answer down this path
            if i >= n or target < 0:
                return False
            
            # If we already found an answer for this path, then return the answer
            if memo[i][target] != -1:
                return memo[i][target]
            
            # If we haven't found an answer yet, then calculate the answer by making
            # the decision to either skip the value at the current index, or choose the 
            # value at the current index.
            memo[i][target] = (dfs(i + 1, target) or dfs(i + 1, target - nums[i]))
            
            # Return the answer you found above
            return memo[i][target]
        
        # Start by running dfs at the first index and the target value, which
        # is half the sum of the original array.
        return dfs(0, target)