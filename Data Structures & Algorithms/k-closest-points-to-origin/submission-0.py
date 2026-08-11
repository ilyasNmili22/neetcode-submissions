class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            points[i].append((points[i][0] ** 2 + points[i][1] ** 2))
        points.sort(key = lambda x: x[2])
        print(points)
        return [point[:2] for point in points[:k]]