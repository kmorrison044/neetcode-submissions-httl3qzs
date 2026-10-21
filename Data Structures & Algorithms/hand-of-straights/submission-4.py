class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        count = Counter(hand)
        for num in hand:
            start = num
            while count[start - 1] > 0:
                start -= 1
            while count[start] > 0:
                for i in range(start, start + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True