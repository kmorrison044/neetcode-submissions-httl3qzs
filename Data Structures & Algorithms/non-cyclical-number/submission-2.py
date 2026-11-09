class Solution:
    def isHappy(self, n: int) -> bool:
        # This is a linked list problem! We can use Floyd's algorithm
        # to find the start of a cycle. This ensures we do not use
        # extra space.
        slow = fast = n

        # This detects the cycle, but does not gaurentee that where we
        # detected the cycle is the start of the cycle.
        while True:
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            slow = self.sumOfSquares(slow)
            if slow == fast:
                break
        
        # This portion finds where the start of the cycle is. There is a proof
        # that demonstrates that the distance between the start of the linked list to the
        # start of the cycle is the exact same distance as where we detected the cycle to 
        # the start of the cycle. Therefore we put another pointer at the beginning and iterate
        # the pointer at the beginning and the pointer where we detected the cycle by 1 until 
        # we reach the start of the cycle.
        slow2 = n
        while slow != slow2:
            slow = self.sumOfSquares(slow)
            slow2 = self.sumOfSquares(slow2)
        
        # If the start of the cycle is 1, then return true, otherwise, return false
        return True if slow == 1 else False

    # This defines the sum of squares calculation
    def sumOfSquares(self, num):
        output = 0

        while num != 0:
            # grabs the last digit
            digit = num % 10
            # updates the output
            output += digit ** 2
            # shrinks num by 1 digit to get the next "last digit".
            # this will eventually become 0.
            num //= 10
        
        return output