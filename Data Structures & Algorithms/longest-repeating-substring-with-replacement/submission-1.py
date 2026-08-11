class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, mx = 0, 0, 0
        res = 0
        my_dict = {}
        while (r < len(s)):
            if s[r] in my_dict:
                my_dict[s[r]] += 1
            else:
                my_dict[s[r]] = 1
            mx = max(my_dict.values())
            
            while (l <= r and r - l + 1 - mx > k):
                my_dict[s[l]] -= 1
                mx = max(my_dict.values())
                l += 1
            if r - l + 1 - mx <= k:
                res = max(res, r - l + 1)
            
            r += 1
        return res
