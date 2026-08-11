class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        my_heap = []
        heapq.heapify(my_heap)
        for i in range(k - 1):
            heapq.heappush(my_heap,(-nums[i], i))

        for i in range(k - 1, len(nums)):
            while (my_heap and nums[i] < -my_heap[0][0] and i - my_heap[0][1] >= k): 
                heapq.heappop(my_heap)
            heapq.heappush(my_heap, (-nums[i], i))
            ret.append(-my_heap[0][0])
            #print(my_heap)
        return ret