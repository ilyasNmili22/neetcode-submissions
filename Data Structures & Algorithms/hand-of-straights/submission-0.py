class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        count = dict(sorted(count.items(), key = lambda x: x[0]))
        for x in count:
            while (count[x]):
                for i in range(groupSize):
                    if x + i in count and count[x + i] > 0:
                        count[x + i] -= 1
                    else:
                        return False
        return True