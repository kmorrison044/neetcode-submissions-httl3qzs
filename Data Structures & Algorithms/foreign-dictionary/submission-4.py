class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        n = len(words)
        for i in range(0, n - 1):
            word1 = words[i]
            word2 = words[i + 1]
            minLen = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            for j in range(minLen):
                if word1[j] != word2[j]:
                    adj.setdefault(word1[j], set()).add(word2[j])
                    break
            
        visited = set()
        path = set()
        ret = []

        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True
            visited.add(node)
            path.add(node)

            for nei in adj.get(node, []):
                if not dfs(nei):
                    return False
            
            path.remove(node)
            ret.append(node)
            return True
        
        for node in adj:
            if not dfs(node):
                return ""
        
        ret.reverse()
        return "".join(ret)
            