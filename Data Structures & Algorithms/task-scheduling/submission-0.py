class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        count = Counter(tasks)

        h = [-cnt for cnt in count.values()]
        heapq.heapify(h)
        q = deque()

        while q or h:
            time += 1

            if h:
                cnt = 1 + heapq.heappop(h)
                if cnt:
                    q.append((cnt, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(h, q.popleft()[0])
        
        return time

