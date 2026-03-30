class Solution:
    def climbStairs(self, n: int) -> int:
        # Do a bottom up DP approach. Starting from the base case (n),
        # how many ways can we get to n? We can get to n 0 ways since we are there already.
        # From n - 1, we can only get to n one way, so one = 1 and two = 0.
        # We go backwards and shift the pointers over 1 postion, making one its 
        # initial value plus two's value and making two one's intial value.
        # We do this n times and return our first pointer.
        one, two = 1, 0

        for i in range(n):
            temp = one
            one = one + two
            two = temp
        
        return one