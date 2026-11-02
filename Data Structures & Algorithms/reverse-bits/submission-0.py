class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0

        for i in range(32):
            # Grab the ith bit (when i is 0, you are grabbing the last bit)
            bit = (n >> i) & 1
            # Update out by using OR (keeps all previous bits the same and 
            # "adds" the current bit). When i is 0, you are putting it in 
            # the place of the first bit, essentially reversing the bits.
            out |= (bit << (31 - i))

        return out