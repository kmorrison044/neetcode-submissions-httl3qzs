class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        i = 0
        check = True

        while True:
            if i >= len(strs[0]):
                return res

            curr = strs[0][i]
            for s in strs: 
                if i >= len(s) or s[i] != curr:
                    return res
            
            res += curr
            i += 1

                
