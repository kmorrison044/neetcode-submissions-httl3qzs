class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Heirholzer's Algorithm. This algorithm finds an Eulerian Path,
        # which is a path through a graph that visits every single edge exactly
        # once. It basically finds dead-ends from finish to start. Since we are sorting
        # and reversing the order, everytime we pop from the adj list, we are getting
        # the lexicographically smallest order.

        adj = {}
        # Create adjacency list in lexographically descending order.
        # This is so that we can pop from the adjacency list with the
        # smallest airport as the result.
        for src, dest in sorted(tickets)[::-1]:
            adj.setdefault(src, []).append(dest)
        
        res = []
        def dfs(src):
            # Iterate while the adjacency list for the current node has elements. This
            # will cause the algorithm to construct the result from final destination back
            # to the starting point.
            while adj.get(src):
                # Grab the smallest destination by popping from the adjacency list.
                # Once everything is popped, the above while loop will break out.
                # Essentially we are destroying this edge on the fly so we don't 
                # travel on it again.
                dst = adj[src].pop()
                # Run dfs on this destination. Once 
                dfs(dst)
            # Once loop is done, add the current node to the result. This is called Post-order
            # travelling.
            res.append(src)
        
        dfs("JFK")
        # List was built from final destination to starting point, so reverse for the answer.
        return res[::-1]