class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # We know there is no solution if this is the case:
        if sum(gas) < sum(cost):
            return -1
        
        # Keep track of what is in our tank and where the current potential start is
        tank = 0
        start = 0
        # Iterate through the list
        for i in range(len(gas)):
            # Add the difference in the tank
            tank += (gas[i] - cost[i])

            # If our tank ever drops below 0, then we know that everywhere between
            # the intial starting point and the current index is invalid, since they
            # will all drop below 0 at the current index, so we simply reset our tank to 0
            # and move our start to the next valid index.
            if tank < 0:
                tank = 0
                start = i + 1
        
        # The valid starting index is the one which is the first place where the tank never drops
        # below 0 again.
        return start