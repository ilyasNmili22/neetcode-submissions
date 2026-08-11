class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            l = str(len(s))
            l = "0" * (3 - len(l)) + l
            encoded += (l + s)
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while (i < len(s)):
            l = int(s[i:i + 3])
            i += 3
            decoded.append(s[i:i + l])
            i += l
        return decoded

            
