class Solution: 	
	def permute(self,nums: List[int]) -> List[List[int]]:
		ret = []
		def backtrack(permutations, used):
			if len(permutations) == len(nums):
				ret.append(permutations[:])
				return
			for i in range(len(nums)):
				if not used[i]:
					used[i] = True
					permutations.append(nums[i])
					backtrack(permutations, used)
					permutations.pop()
					used[i] = False	
		backtrack([], len(nums) * [False])
		return ret