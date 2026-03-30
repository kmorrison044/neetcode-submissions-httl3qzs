class Solution:
    def numDecodings(self, s: str) -> int:
        # At every index we have two choices: analyze the current index character,
        # or analyze the current character and the next character. If we get to the
        # end of the list, then we have a solution. We can start from the back of
        # the list and work backwards to get the answer using two variables to save
        # memory. 
        n = len(s)
        res1, res2 = 1, 0

        for i in range(n - 1, -1 , -1):
            # First set the temp variable, so we can set res1 to it later.
            # If the current character is invalid, then we score a 0, if it is valid,
            # then we set temp to whatever res1 is currently.
            if s[i] == '0':
                temp = 0
            else:
                temp = res1
            
            # Check if the next character qualifies as a valid number.
            if (i < n - 1 and (s[i] == '1' or s[i] == '2' and int(s[i + 1]) < 7)):
                # If it is valid, then add res2's value to temp.
                temp += res2
            
            # Finally reset temp, set res1 to temp and res2 to res1
            temp, res1, res2 = 0, temp, res1
        
        # res1 represents the current index, so return it.
        return res1