class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = 0, 0, 0
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            if triplet[0] == target[0]:
                a = 1
            if triplet[1] == target[1]:
                b = 1
            if triplet[2] == target[2]:
                c = 1
            if a == b == c == 1:
                return True
        return False