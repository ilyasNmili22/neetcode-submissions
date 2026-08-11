from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        target = Counter(t)
        
        l, count = 0, 0
        min_len, start_index = float('inf'), 0
        required = len(t)
        
        for r in range(len(s)):
            # Check if the current char exists in our target Counter keys
            if s[r] in target:
                target[s[r]] -= 1
                # If the count is >= 0, it means we actually needed this instance
                if target[s[r]] >= 0:
                    count += 1
            
            # Shrink the window while it is valid (contains all chars from t)
            while count == required:
                # Update minimum length if this window is smaller
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    start_index = l
                
                # Try to remove the character at the left pointer
                if s[l] in target:
                    target[s[l]] += 1
                    # If count becomes positive, we lost a required character
                    if target[s[l]] > 0:
                        count -= 1
                l += 1
                
        return "" if min_len == float('inf') else s[start_index : start_index + min_len]