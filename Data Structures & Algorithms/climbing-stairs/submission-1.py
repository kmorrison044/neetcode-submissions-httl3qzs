class Solution:
    def climbStairs(self, n: int) -> int:
        # Do a bottom up DP approach. Starting from the base case (n),
        # how many ways can we get to n? We can get to n only 1 way.
        # From n - 1, we can also get to n one way, so one = 1 and two = 1.
        # We go backwards and shift the pointers over 1 postion, making one its 
        # initial value plus two's value and making two one's intial value.
        # We do this n-1 times and return our first pointer.
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one