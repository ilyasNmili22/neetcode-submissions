class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = r = mx = 0
        mx_occ = 0
        for r in range(len(s)):
            count[s[r]] += 1
            mx_occ = max(mx_occ, count[s[r]])
            if r - l + 1 - mx_occ <= k:
                mx = max(mx, r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1
        return mx