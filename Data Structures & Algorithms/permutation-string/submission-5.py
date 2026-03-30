class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        str1 = [0]*26
        str2 = [0]*26

        for c in s1:
            str1[ord(c) - ord('a')] += 1
        
        for i in range(len(s2)):
            str2[ord(s2[i])-ord('a')] += 1
            if i > len(s1)-1:
                str2[ord(s2[i-len(s1)]) - ord('a')] -= 1
            if str1 == str2:
                return True
        
        return False
