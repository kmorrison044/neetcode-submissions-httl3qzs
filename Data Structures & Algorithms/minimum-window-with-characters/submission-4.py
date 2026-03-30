class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Count required characters
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        missing = len(t)          # total chars still needed
        left = 0
        best_start = 0
        best_len = float('inf')

        for right in range(len(s)):
            c = s[right]

            if c in need:
                if need[c] > 0:
                    missing -= 1
                need[c] -= 1

            # Try to shrink the window while it's valid
            while missing == 0:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left

                left_char = s[left]
                if left_char in need:
                    need[left_char] += 1
                    if need[left_char] > 0:
                        missing += 1

                left += 1

        return "" if best_len == float('inf') else s[best_start:best_start + best_len]
