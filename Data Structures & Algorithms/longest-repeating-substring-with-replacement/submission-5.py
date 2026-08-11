class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, mx, res = 0, 0, 0
        my_dict = {}
        
        for r in range(len(s)):
            if s[r] in my_dict:
                my_dict[s[r]] += 1
            else:
                my_dict[s[r]] = 1
            
            mx = max(mx, my_dict[s[r]])
            
            while (r - l + 1) - mx > k:
                my_dict[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            
        return res