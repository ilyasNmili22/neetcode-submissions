class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        for i in range(len(temperatures)):
            j = 1
            while(i + j < len(temperatures) and temperatures[i + j] <= temperatures[i]):
                j += 1
            if i + j == len(temperatures):
                s.append(0)
            else:
                s.append(j)
        return s