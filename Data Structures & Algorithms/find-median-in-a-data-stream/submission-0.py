class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        

    def findMedian(self) -> float:
        self.nums.sort()

        n = len(self.nums)
        if n % 2 == 0:
            r = n // 2
            l = r - 1

            return (self.nums[r] + self.nums[l]) / 2
        else:
            i = n // 2
            return self.nums[i]