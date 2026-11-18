class Solution:
    def myPow(self, x: float, n: int) -> float:
        power = abs(n)
        res = 1
        while power != 0:
            if power & 1:
                res *= x
            x *= x
            power >>= 1
        
        return res if n > 0 else 1 / res
        
