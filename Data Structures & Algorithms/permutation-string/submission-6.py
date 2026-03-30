class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Elegant algorithm where you compare character array
        # counts and slide the window every iteration and adjust
        # character counts as needed. Runs O(n) time and O(1) space.
        
        # Initialize character arrays
        str1 = [0]*26
        str2 = [0]*26

        # Get count of desired permutation string
        for c in s1:
            str1[ord(c) - ord('a')] += 1
        
        # Loop through the check string.
        for i in range(len(s2)):
            # Add to the count
            str2[ord(s2[i])-ord('a')] += 1

            # If index moves past window (which is the length
            # of s1), then subtract 1 from the count of the leftmost
            # element of the window.
            if i > len(s1)-1:
                str2[ord(s2[i-len(s1)]) - ord('a')] -= 1
            
            # If both character arrays are equal, then we found
            # a permutation.
            if str1 == str2:
                return True
        
        return False
