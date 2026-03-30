class Solution:
    def isPalindrome(self, s: str) -> bool:
        check_str = ''
        for ch in s:
            if ch.isalnum():
                check_str += ch.lower()
        return check_str == check_str[::-1]