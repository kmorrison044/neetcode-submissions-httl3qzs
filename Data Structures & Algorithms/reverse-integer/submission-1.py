class Solution:
    def reverse(self, x: int) -> int:
        max_int = 0x7FFFFFFF
        min_int = -0x7FFFFFFF - 1
        res = 0

        while x != 0:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            if res > max_int // 10 or (res == max_int // 10 and digit > max_int % 10):
                return 0
            if res < min_int // 10 or (res == min_int // 10 and digit < min_int % 10):
                return 0
            
            res = (res * 10) + digit
        
        return res
