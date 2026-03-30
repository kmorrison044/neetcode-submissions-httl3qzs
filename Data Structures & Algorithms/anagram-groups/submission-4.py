class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = {}
        for s in strs:
            key = 26 * [0]
            for c in s:
                key[ord(c) - ord('a')] += 1
            ret.setdefault(tuple(key), []).append(s)

        return list(ret.values())