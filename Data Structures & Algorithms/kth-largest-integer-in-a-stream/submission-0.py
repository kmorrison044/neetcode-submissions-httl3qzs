class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Store k, store nums in minHeap
        self.k = k
        self.minHeap = nums
        # heapify the minHeap
        heapq.heapify(self.minHeap)
        # We only want to keep the k largest elements in the min heap.
        # In order to store this amount, keep popping elements out of
        # the heap until the length of the heap is equal to k.
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # We currently have the k largest elements in the heap upon
        # initialization. Add a new value to the heap, and if the len of
        # the heap is greater than k, pop the heap.
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        # The smallest of the k largest elements is the root of the heap
        # This is an O(1) operation.
        return self.minHeap[0]
        
