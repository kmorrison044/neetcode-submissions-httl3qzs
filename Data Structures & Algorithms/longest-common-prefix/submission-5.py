class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        i = 0

        # Scan column by column in each string and see if there is a difference,
        # or if i goes out of range of any string in strs.
        while True:
            for s in strs: 
                if i >= len(s) or s[i] != strs[0][i]:
                    return "".join(res)
            
            res.append(strs[0][i])
            i += 1

                
