class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = False
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        
        digits.append(0)
        for i in range(len(digits) - 2, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                digits.pop()
                return digits
            else:
                if i == 0:
                    digits[i] = 1
                else:
                    digits[i] = 0
        return digits