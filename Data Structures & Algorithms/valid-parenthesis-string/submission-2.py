class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin = leftMax = 0

        for c in s:
            if c == '(':
                # Increment our possible min left parenthesis and max left parenthesis
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ')':
                # Decrement our possible min left parenthesis and max left parenthesis
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                # If wildcard, decrement possible min left parenthesis
                # and increment max left parenthesis, since wildcard could
                # be either a '(' or ')'.
                leftMin, leftMax = leftMin - 1, leftMax + 1
            
            # If leftMax drops below 0, that means we have more right parenthesis
            # than left at some point, so return False
            if leftMax < 0:
                return False
            # If leftMin drops below 0, it is still possible that we have enough
            # left parenthesis to match the righ parenthesis (given leftMax > 0),
            # so we reset to 0, because if it is negative, then it is no longer valid.
            # This means we needed to choose SOME of the wildcards to be empty strings,
            # thus we reset it to 0 because we could've chosen some to be empty wildcards
            # and then leftMin could be 0.
            if leftMin < 0:
                leftMin = 0
        # If leftMin == 0, then we have exactly the number of left parenthesis as right
        # parenthesis, so return true.
        return leftMin == 0