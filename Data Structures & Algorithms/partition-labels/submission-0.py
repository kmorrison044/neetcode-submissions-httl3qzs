class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        
        curr = set()
        ret = []
        i = 0
        while i < len(s):
            curr.add(s[i])
            start = i
            while curr:
                if s[i] not in curr:
                    curr.add(s[i])
                if s[i] in curr and count[s[i]] > 0:
                    count[s[i]] -= 1
                if count[s[i]] == 0:
                    curr.remove(s[i])
                i += 1
            ret.append(i - start)
        
        return ret