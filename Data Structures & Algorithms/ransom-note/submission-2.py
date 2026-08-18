class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = 26 * [0]
        for x in magazine:
            freq[ord(x) - ord('a')] += 1
        for x in ransomNote:
            freq[ord(x) - ord('a')] -= 1
        return True if all(freq[i] >= 0 for i in range(26)) else False