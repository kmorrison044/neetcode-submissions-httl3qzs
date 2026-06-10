class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra's Algo
        adj = {}
        # Create an adjacency list that maps nodes to neighbors directly
        for s, e, t in times:
            adj.setdefault(s, []).append([e, t])
        
        # Keep track of a times list that finds the shortest path
        # for each node in the graph.
        times = [float('inf') for node in range(n + 1)]
        # Since these are 1 indexed, set index 0 to -inf
        times[0] = float('-inf')
        # The start node to itself takes 0 time
        times[k] = 0
        # Keep track of a visit set to determine if all nodes recevied
        # the signal
        visit = set()

        # Create a heap to store nodes to be visited
        q = [(0, k)]

        while q:
            # Grab current node in the queue
            curr_time, curr_node = heapq.heappop(q)

            # If we already recorded a time that is shorter to the node than this edge,
            # skip the node
            if curr_time > times[curr_node]:
                continue

            # At this point we have visited the node. Since the next step is
            # to process it.
            visit.add(curr_node)
            
            # Run through the neighbors of the current node.
            for nei, edge_time in adj.get(curr_node, []):
                # Calculate the time it takes to get to the neighbor node from
                # the current node.
                new_time = curr_time + edge_time

                # If this time is less than an already recorded time to get to this neighbor,
                # then update the recorded time and push the new time and neighbor into the q.
                if new_time < times[nei]:
                    times[nei] = new_time
                    heapq.heappush(q, (new_time, nei))

        # We want the longest time to get to all nodes. This is the max value in the times
        # list if all nodes were visited. If not, then return -1 as per the requirement.
        return max(times) if len(visit) == n else -1