class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        def helper(x, power):
            if power == 0:
                return 1.0
            if x == 0:
                return 0.0
            res = helper(x * x, power // 2)
            return res if power % 2 == 0 else res * x

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res