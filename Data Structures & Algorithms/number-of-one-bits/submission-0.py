class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        # While n is greater than 0 (we are effectively dividing by 2 evey iteration)
        while n > 0:
            # If the last bit is one, increment the count
            if n & 1 == 1:
                count += 1
            # Shift the bits over by one. This increments the count everytime
            # the last bit is one. Once n has no more bits, then return count.
            n >>= 1
        return count