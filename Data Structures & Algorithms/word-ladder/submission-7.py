class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Use a hashset for O(1) lookups
        words, res = set(wordList), 0

        # Check base case
        if (endWord not in words) or (beginWord == endWord):
            return 0
        
        # Run a classic bfs. We will find the neighbors of each node on the fly.
        # Add the beginning word to the q.
        q = deque([beginWord])
        while q:
            # Increment res after exploring each layer of bfs
            res += 1
            # Analyze each word in the currently in the queue so that
            # we fully analyze a layer prior to incrementing res.
            for _ in range(len(q)):
                # Grab the word
                word = q.popleft()
                # If that word is the end word, we are done. Return res
                if word == endWord:
                    return res

                # This is the clunky part. In order to find the neighbors of the current
                # word, and because the requirement says that the neighbors can only differ by
                # one character, then we loop through each potential character (a - z), then loop
                # through each character in the word and replace it with the potential character.
                for ch in range(ord('a'), ord('z') + 1):
                    for i in range(len(word)):
                        if chr(ch) == word[i]:
                            continue
                        # Construct the potential word
                        pot = word[:i] + chr(ch) + word[i + 1:]
                        # if it is in the word list, then we found a neighbor
                        if pot in words:
                            # append to the q and remove it from the word list to indicate we
                            # have visited it.
                            q.append(pot)
                            words.remove(pot)
        return 0
