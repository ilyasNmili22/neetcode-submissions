class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        my_dict = {}
        for i, x in enumerate(s):
            my_dict[x] = i
        ret = []
        l = mx = 0
        for r in range(len(s)):
            mx = max(mx, my_dict[s[r]])
            if r == mx:
                ret.append(r - l + 1)
                l = r + 1
        return ret      



'''
'xyxxy' 'zbzbb' 'i' 's' 'l'
x = 4
y = 5
z = 8
b = 10
i = 11
s = 12
l = 13


'''