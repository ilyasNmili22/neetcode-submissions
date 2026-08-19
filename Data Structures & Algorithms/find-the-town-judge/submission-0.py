class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        my_dict = {}
        ans = -1
        for x in trust:
            my_dict[x[0]] = -1
            if ans == x[0]:
                ans = -1 
            #print(my_dict)
            if x[1] not in my_dict or my_dict[x[1]] != -1:
                my_dict[x[1]] = my_dict.get(x[1], 0) + 1
                if my_dict[x[1]] == n - 1:
                    ans = x[1]
        return ans