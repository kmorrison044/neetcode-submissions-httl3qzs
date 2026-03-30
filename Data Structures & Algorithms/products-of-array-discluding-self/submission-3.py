class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        total = 1
        count = 0

        for n in nums:
            if n == 0:
                count += 1
                if count > 1:
                    return [0] * len(nums)
                continue
            total *= n

        for n in nums:
            if n == 0:
                output.append(total//1)
            else:
                if count == 0:
                    output.append(total//n)
                else:
                    output.append(0)

        return output