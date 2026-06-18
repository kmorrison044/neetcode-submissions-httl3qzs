class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # This question is hard if you take the question literally and
        # actually try to solve how you would arrange everything to be perfect.
        # An easy way to solve it is to just count the occurrences of each character in 
        # all the words and see if they are divisble evenly across all words. This works
        # because we can arrange the characters any way we would like, so we just need to
        # know if we can evenly distribute the characters across all words in any order.
        n = len(words)
        count = {}

        # Count the number of characters
        for word in words:
            for char in word:
                count[char] = count.get(char, 0) + 1
        
        # See if the character count can be distributed evenly
        # across all words
        for char in count:
            if count[char] % len(words):
                return False
        
        return True