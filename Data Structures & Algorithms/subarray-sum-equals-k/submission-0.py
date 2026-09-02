class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        my_dict = {0 : 1}
        ans = 0
        s = 0
        for x in nums:
            s += x
            if s - k in my_dict:
                ans += my_dict[s - k]
            if s in my_dict:
                my_dict[s] += 1
            else:
                my_dict[s] = 1
        return ans

"""
2 -1 1 2


0 ->1
2 ->1
1 > 1
2 -> 2
4 -> 1

"""