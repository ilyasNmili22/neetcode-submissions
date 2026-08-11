class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        data = [(p, s) for (p, s) in zip(position, speed)]
        # print(*zip(position, speed)): (4, 2) (1, 2) (0, 1) (7, 1)
        data.sort(reverse = True)
        for p,s in data:
            time = (target - p) / s
            if not stack or time > stack[-1]:  
                stack.append(time)
            
        return len(stack)