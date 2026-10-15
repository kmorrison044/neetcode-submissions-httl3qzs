class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman-Ford Algo

        # Intialize prices array to be inf
        prices = [float("inf")] * n
        # Price to get to the source node is 0
        prices[src] = 0

        # Do BFS k + 1 times. That is, you do k + 1 layers of BFS, because k stops is k + 1 layers
        # of BFS
        for _ in range(k + 1):
            # Keep a tmpPrices array to store the cost to get to nodes at the current layer
            tmpPrices = prices.copy()
            # Iterate through all edges
            for s, d, p in flights:
                # If the price to get to the current edge is infinity, the skip processing
                if prices[s] == float("inf"):
                    continue
                # Update the temp prices list to be the minimum of its current value and
                # the current cost to get to the source node plus the price to go from the
                # source node to the destination node
                tmpPrices[d] = min(tmpPrices[d], prices[s] + p)
            # Update the prices list to be the copy of the temp prices list
            prices = tmpPrices.copy()
        
        # If it is impossible to get to the destination in k stops, then return -1,
        # otherwise return the price to get to the target node.
        return -1 if prices[dst] == float("inf") else prices[dst]
