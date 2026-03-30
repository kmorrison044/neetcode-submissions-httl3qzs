class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        maj = (float("-inf"), None)

        for n in nums:
            curr = count[n] = count.setdefault(n, 0) + 1
            if curr > maj[0]:
                maj = (curr, n)
            print("n is:", n)
            print("curr is:", curr)
            print("maj is:", maj)
            print("\n")
        
        return maj[1]