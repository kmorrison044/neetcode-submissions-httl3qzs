class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def build_map(word):
            mem_map = {}
            for c in word:
                #mem_map[c] = 1 + mem_map.get(c, 0)
                mem_map [c] = mem_map.setdefault(c, 0) + 1
            return mem_map
        return build_map(s) == build_map(t)
