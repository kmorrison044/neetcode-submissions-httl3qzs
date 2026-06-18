class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        tickets.sort()

        for node, nei in tickets:
            adj.setdefault(node, []).append(nei)
        
        ret = ['JFK']
        def dfs(node):
            if len(ret) == len(tickets) + 1:
                return True
            if node not in adj:
                return False

            neighbors = adj[node].copy()
            for i, v in enumerate(neighbors):
                adj[node].pop(i)
                ret.append(v)
                if dfs(v): return True
                ret.pop()
                adj[node].insert(i, v)
                
            return False

        dfs('JFK')
        return ret