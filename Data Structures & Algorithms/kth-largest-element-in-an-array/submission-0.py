class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1
        heapq.heapify(nums)
        for i in range(k - 1):
            heapq.heappop(nums)

        return -nums[0]


'''
[3,2,1,5,6,4], k = 2
[-3,-2,-1,-5,-6,-4], k = 2
'''