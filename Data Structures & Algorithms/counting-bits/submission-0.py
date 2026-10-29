class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOnes(num):
            count = 0
            while num > 0:
                if num & 1 == 1:
                    count += 1
                num >>= 1
            return count
        
        out = []
        for i in range(0, n + 1):
            out.append(countOnes(i))
        
        return out

