import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance=[(-math.sqrt(points[i][0]**2 + points[i][1]**2),i) for i in range(len(points))]
        heapq.heapify(distance)

        while len(distance)>k :
            heapq.heappop(distance)

        return [points[dist[1]] for dist in distance]
       