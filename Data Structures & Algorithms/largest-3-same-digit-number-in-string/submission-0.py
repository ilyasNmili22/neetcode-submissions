class Solution:
    def largestGoodInteger(self, num: str) -> str:
        x = []
        for i in range(10):
            x.append(3 * chr(ord('0') + i))
        x.reverse()
        for a in x:
            if a in num:
                return a
        return '' 