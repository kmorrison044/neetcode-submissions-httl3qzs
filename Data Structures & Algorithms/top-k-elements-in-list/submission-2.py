class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            hmap[n] = hmap.setdefault(n, 0) + 1
        for key, value in hmap.items():
            freq[value].append(key)
        
        ret = []
        for i in range(len(freq) - 1, 0, -1):
            #for n in freq[i]: # Because each answer is unique, we can just extend the ret list
            #    ret.append(n)
            ret.extend(freq[i])
            if len(ret) == k:
                return ret