class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(leftarr, rightarr):
            l, r = 0, 0
            ans = []
            while (l < len(leftarr) and r < len(rightarr)):
                if leftarr[l] < rightarr[r]:
                    ans.append(leftarr[l])
                    l += 1
                else:
                    ans.append(rightarr[r])
                    r += 1
            ans.extend(leftarr[l:])
            ans.extend(rightarr[r:])
            return ans
        n = len(nums)
        m = n // 2
        if n == 1:
            return nums

        lefty = self.sortArray(nums[:m])
        righty = self.sortArray(nums[m:])
        return merge(lefty, righty)