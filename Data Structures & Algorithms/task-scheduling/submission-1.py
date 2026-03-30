class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        # Count how many times a certain task needs to be processed
        count = Counter(tasks)

        # Get all of the times each task needs to be processed and create
        # a max heap of the counts to process the tasks that have the most
        # counts left first
        h = [-cnt for cnt in count.values()]
        heapq.heapify(h)

        # Create a deque that stores the remaining number of times a task
        # needs to be processed with the time it can be run again after
        # cool down.
        q = deque()
        # Iterate while either the q or the heap has elements left, meaning we
        # still have tasks to process.
        while q or h:
            # Increment the time at each iteration of the loop
            time += 1

            # If the heap is non empty, process a task
            if h:
                # We are processing the task with the most counts left.
                # Decrement the count (since a max heap, add 1, since all
                # values are negative)
                cnt = 1 + heapq.heappop(h)
                # If the count is non-zero, there are still remaining times
                # the task must be run, so add its count and the time at which
                # it can be run again to the q (which is time + n)
                if cnt:
                    q.append((cnt, time + n))
            
            # if the q is non-empty and the first value's time equals the 
            # current time, add the task to the heap.
            if q and q[0][1] == time:
                heapq.heappush(h, q.popleft()[0])
        
        # Once we are out of the loop, just return the time it took to empty
        # the heap and deque.
        return time

