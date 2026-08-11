class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        res = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num2)):
            for j in range(len(num1)):
                m = (ord(num2[i]) - ord('0')) * (ord(num1[j]) - ord('0')) + res[i + j]
                res[i + j] = m % 10
                res[i + j + 1] += m // 10

        res = res[::-1]
        i = 0
        while (res[i] == 0):
            i += 1
        res = [str(x) for x in res[i:]]

        return ''.join(res)