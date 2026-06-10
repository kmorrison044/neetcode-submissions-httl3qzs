class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for s, e, t in times:
            adj.setdefault(s, []).append([e, t])
        
        times = {node + 1: float('inf') for node in range(n)}
        times[k] = 0
        visit = set()

        q = [(0, k)]

        while q:
            curr_time, curr_node = heapq.heappop(q)

            if curr_time > times[curr_node]:
                continue
                
            visit.add(curr_node)
            
            for nei, edge_time in adj.get(curr_node, []):
                new_time = curr_time + edge_time

                if new_time < times[nei]:
                    times[nei] = new_time
                    heapq.heappush(q, (new_time, nei))
            
        return max(times.values()) if len(visit) == n else -1