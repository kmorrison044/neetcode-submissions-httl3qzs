class MedianFinder:

    def __init__(self):
        self.nums = []
        self.n = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.nums, num)
        self.n += 1

    def findMedian(self) -> float:
        temp = []
        ret = 0
        i = 0
        if self.n % 2 == 0:
            while i < (self.n // 2) - 1:
                temp.append(heapq.heappop(self.nums))
                i += 1
            l = heapq.heappop(self.nums)
            temp.append(l)
            r = heapq.heappop(self.nums)
            temp.append(r)
            ret = (l + r) / 2 

        else:
            while i < (self.n // 2) + 1:
                ret = heapq.heappop(self.nums)
                temp.append(ret)
                i += 1

        while temp:
            heapq.heappush(self.nums, heapq.heappop(temp))

        return ret