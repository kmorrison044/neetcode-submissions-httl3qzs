class MedianFinder:

    def __init__(self):
        # Create a small and large heap where the small heap contians the smaller half 
        # of numbers coming in with the largest on top and the large heap contains the
        # larger half of numbers coming in with the smallest on top
        self.large = []
        self.small = []
        # Total number of elements seen
        self.n = 0

    def addNum(self, num: int) -> None:
        self.n += 1
        # If the current number is larger than the smallest
        # element in the large heap, add it to the large heap,
        # otherwise, add it to the small heap
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        # Adjust heaps to make them equal in size
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        # If the heaps are even, then return the avg of the top elements
        # in each heap
        if self.n % 2 == 0:
            return (self.large[0] + (-self.small[0])) / 2
        # If not even, the heap with the most elements contians the median
        if len(self.large) > len(self.small):
            return self.large[0]
        else:
            return -self.small[0]


