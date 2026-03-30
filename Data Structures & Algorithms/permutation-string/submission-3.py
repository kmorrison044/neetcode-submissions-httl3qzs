class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = r = 0
        count = {}
        for c in s1:
            count[c] = count.setdefault(c, 0) + 1

        curr = count.copy()
        while r < len(s2):
            if s2[r] in curr:
                curr[s2[r]] -= 1
                if curr[s2[r]] == 0:
                    del curr[s2[r]]
                if len(curr) == 0:
                    return True
                r+=1
            else:
                curr = count.copy()
                l += 1
                r = l
            print(curr)
        
        return False
            
                


            