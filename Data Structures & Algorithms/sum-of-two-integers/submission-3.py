class Solution:
    def getSum(self, a: int, b: int) -> int:
        # To sum 2 integers in binary, you essentially AND them together and shift
        # left to get the carry, and then XOR the 2 numbers together until the carry 
        # equals 0.

        # Python does not restrain variables to be 32 bits, so we need a mask to keep it
        # 32 bits. We also need the max value a 32 bit integer could be.
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFF

        # We are going to make b the carry, so keep going until b is 0.
        while b != 0:
            # Compute the carry between the XOR (a) and the previous carry (b).
            # Shift left by 1.
            carry = (a & b) << 1
            # XOR the previous addition and the previous carry. Make sure it stays 32 by
            # applying the mask to it.
            a = (a ^ b) & mask
            # update the new carry (b) by assigning it to the carry calculated above and
            # applying the mask.
            b = carry & mask
        
        # If a is less than the max int, then it is positive, we can return a.
        # If it is greater than the max int, the first bit which represents positive
        # or negative will be 1 (negative) and thus in pure binary is greater than
        # the max of a signed int. Therefore we convert it to the negative number by
        # using the XOR and not trick
        return a if a <= max_int else ~(a ^ mask)