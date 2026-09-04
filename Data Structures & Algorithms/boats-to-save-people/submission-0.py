class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        s = 0
        while (l <= r):
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            s += 1
        return s

"""
1 2 4 5

1, 5

"""