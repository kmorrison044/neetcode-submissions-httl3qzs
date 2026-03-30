class Solution:
    def isPalindrome(self, s: str) -> bool:
        special_ch = ["*", "!", ".", "(", ")", "?", " ", ",", "'", ":"]
        s = ''.join([c for c in s if c not in special_ch])
        s = s.lower()
        print(s)
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True