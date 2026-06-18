class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        # Sort tickets to get them in lexicographically smallest order
        tickets.sort()

        # Create adj list
        for node, nei in tickets:
            adj.setdefault(node, []).append(nei)
        
        # We know JFK in return
        ret = ['JFK']
        def dfs(node):
            # So we know the return value will have 1 more airport than
            # the number of tickets because the tickets represent the edges
            # and the airports represent the nodes. If the return value
            # equals 1 + len(tickets) then we found all airports and can 
            # return
            if len(ret) == len(tickets) + 1:
                return True
            if node not in adj:
                return False

            # Create a temp var for neighbors since we are editing adj[node] 
            # on the fly in the loop
            neighbors = adj[node].copy()
            for i, v in enumerate(neighbors):
                # Pop the value in the list with the corresponding pointer.
                # We do this because based on how the recursion goes, we may
                # need to add it back in the same spot later.
                adj[node].pop(i)
                ret.append(v)
                # We found it, return true.
                if dfs(v): return True
                # So we didn't dfs in the right order if we got here, so remove
                # the node from the return value, then insert that node back into
                # the adjacency list at the proper place.
                ret.pop()
                adj[node].insert(i, v)

            # If we get out of the loop, return false
            return False

        dfs('JFK')
        return ret