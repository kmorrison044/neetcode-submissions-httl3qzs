class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words, res = set(wordList), 0

        if (endWord not in words) or (beginWord == endWord):
            return 0
        
        q = deque([beginWord])
        while q:
            res += 1
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res

                for ch in range(ord('a'), ord('z') + 1):
                    for i in range(len(word)):
                        if chr(ch) == word[i]:
                            continue
                        pot = word[:i] + chr(ch) + word[i + 1:]
                        if pot in words:
                            q.append(pot)
                            words.remove(pot)
        return 0
