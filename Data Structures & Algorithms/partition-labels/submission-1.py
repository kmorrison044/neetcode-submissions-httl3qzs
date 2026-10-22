class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        
        curr = set()
        ret = []
        i = 0
        while i < len(s):
            curr.add(s[i])
            start = i
            while curr:
                if s[i] not in curr:
                    curr.add(s[i])
                if s[i] in curr and count[ord(s[i]) - ord('a')] > 0:
                    count[ord(s[i]) - ord('a')] -= 1
                if count[ord(s[i]) - ord('a')] == 0:
                    curr.remove(s[i])
                i += 1
            ret.append(i - start)
        
        return ret