class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        res1 = res2 = 1

        for i in range(n - 1, -1 , -1):
            if s[i] == '0':
                temp = 0
            else:
                temp = res1
            
            if (i < n - 1 and (s[i] == '1' or s[i] == '2' and int(s[i + 1]) < 7)):
                temp += res2
            
            temp, res1, res2 = 0, temp, res1
        
        return res1