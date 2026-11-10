class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Append a 0 to the end of the list in case we need
        # to increase the most significant digit (O(1) operation).
        digits.append(0)
        # Iterate through the list backwards starting from the end of the original list.
        for i in range(len(digits) - 2, -1, -1):
            # If a digit is less than 9, we can simply increment this one and pop the
            # additional and unnecessary 0 (O(1) operation)
            if digits[i] < 9:
                digits[i] += 1
                digits.pop()
                return digits
            # Otherwise we mark the digit as 0 to carry over. If we are at the begining
            # of the list, we simply mark it as a 1 and the increase in the most significant
            # digit was handled by the 0 we added at the beginning.
            else:
                digits[i] = 1 if i == 0 else 0
        return digits