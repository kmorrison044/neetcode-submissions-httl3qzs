class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = {}
        for s in strs:
            key = [ord(c) for c in s]
            key.sort()
            key = tuple(key)
            print(key)
            ret.setdefault(key, []).append(s)
        lst1 = [ord(c) for c in "duh"]
        lst2 = [ord(c) for c in "ill"]
        #print(lst1)
        #print(lst2)

        return list(ret.values())