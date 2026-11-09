class Solution:
    def isHappy(self, n: int) -> bool:
        m = set()
        num = n
        while True:
            summation = 0
            while num != 0:
                digit = num % 10
                num //= 10
                summation += digit ** 2
            
            if summation == 1:
                return True
            if summation in m:
                return False
            
            num = summation
            m.add(summation)