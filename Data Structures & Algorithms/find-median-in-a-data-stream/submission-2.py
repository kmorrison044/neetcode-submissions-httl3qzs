class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []
        self.n = 0

    def addNum(self, num: int) -> None:
        self.n += 1
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if self.n % 2 == 0:
            return (self.large[0] + (-self.small[0])) / 2
        if len(self.large) > len(self.small):
            return self.large[0]
        else:
            return -self.small[0]


