class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        my_dict = {}
        s = 0
        for x in grid:
            for y in x:
                my_dict[y] = 1 + my_dict.get(y, 0)
                s += 1
        a1, a2 = 0, 0
        for i in range(1, s + 1):
            if i not in my_dict:
                a2 = i
            elif my_dict[i] == 2:
                a1 = i
        return [a1, a2]

        