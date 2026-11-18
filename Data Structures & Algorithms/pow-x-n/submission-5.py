class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Get absolute value of power and we can invert at the end
        power = abs(n)
        # Start with res = 1
        res = 1

        # The power can be viewed in binary representation.
        # For example 5 = 1 * 2^2 + 0 * 2^1 + 1 * 2^0 (101 binary)
        # so x^5 = x^(4 + 0 + 1) = x^4 * x^0 * x^1.
        # The binary representation of the power shows us what bits
        # (powers of 2) are activated to multiply with the final result, so
        # we multiple res by the current activated power of 2.

        # We shift power over by one every iteration so it will eventually equal 0
        while power != 0:
            # If the power of 2 is activated, the multiply with res
            if power & 1 == 1:
                res *= x
            
            # Square x
            x *= x
            # Shift the power
            power >>= 1
        
        # If n is positive, return res, else, return 1 / res
        return res if n > 0 else 1 / res