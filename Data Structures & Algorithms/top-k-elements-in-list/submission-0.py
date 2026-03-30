class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        ret = []
        for n in nums:
            hmap[n] = hmap.setdefault(n, 0) + 1
        
        sorted_it = sorted(hmap.keys(), key=lambda key: hmap[key], reverse=True)

        return sorted_it[:k]
