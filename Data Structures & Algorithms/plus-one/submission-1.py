class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        i = n - 1
        while(i >= 0 and digits[i] == 9):
            i -= 1
        if i != -1:
            return digits[:i] + [digits[i] + 1] +  (n - i - 1) * [0]
        return [1] + n * [0]