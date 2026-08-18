class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = 26 * [0]
        for x in magazine:
            freq[ord(x) - ord('a')] += 1
        for x in ransomNote:
            freq[ord(x) - ord('a')] -= 1
            if freq[ord(x) - ord('a')] < 0:
                return False
        return True