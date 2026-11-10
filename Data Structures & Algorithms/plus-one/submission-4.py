class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.append(0)
        for i in range(len(digits) - 2, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                digits.pop()
                return digits
            else:
                digits[i] = 1 if i == 0 else 0
        return digits