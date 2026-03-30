class Solution:
    def rob(self, nums: List[int]) -> int:
        # initialize two rob vars to 0
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ...]
        # Iterate over nums
        for n in nums:
            # We want to check the previous two values of choices for robbing houses.
            # rob2 is i-1 away from i and rob1 is i-2 away. Our choice is to either rob
            # the current house and add the money robbed two houses ago, or not rob the current house,
            # and take the value up to this point as what we robbed from rob2. We take the max of these values,
            # and set the rob1 equal to rob2 (since we are shifting pointers) and update rob2 to the calculation
            # above (since we are shifting pointers on the next iteration)
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2