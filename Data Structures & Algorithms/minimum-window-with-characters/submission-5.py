class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Basically just adjust window based off if the window contains all the required characters.

        # Check empty or null strings
        if not s or not t:
            return ""

        # Count all characters in desired substr
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        # Create missing var that checks if any characters are missing
        missing = len(t)
        l = 0
        s_ret = 0 # Return value for start of substr
        best_len = float('inf')
        # Loop through the list with r as right pointer
        for r in range(len(s)):
            c = s[r] # Current character

            # If the character is in the substring, then adjust counts
            if c in need:
                # If the count of the character is greater than 0 in the window (i.e
                # it is still needed), then subtract it from missing.
                if need[c] > 0:
                    missing -= 1
                # Subtract the character from the need dict
                need[c] -= 1

            # Adjust the left pointer while the window is still valid
            while missing == 0:
                # Adjust the best length and best start if the valid window is 
                # less than the current best length.
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    s_ret = l

                # Adjust the left pointer by first checking if it is a valid character
                # in the substr, then if valid, add 1 to your need dict, and if need
                # dict key is greater than 0, then add 1 to your missing var
                l_char = s[l]
                if l_char in need:
                    need[l_char] += 1
                    if need[l_char] > 0:
                        missing += 1

                # Increment l in while loop
                l += 1

        # if best_len is still inf, then no valid substr was found, else
        # the best substr is your start index and end index is start index + best lenght
        return "" if best_len == float('inf') else s[s_ret:s_ret + best_len]
