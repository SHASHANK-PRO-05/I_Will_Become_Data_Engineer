# not a completely bad solution
from heapq import *


class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        heap = [(-startFuel, 0)]
        if startFuel >= target:
            return 0
        stations = sorted(stations, key=lambda x: x[0])
        ans = float('inf')
        for i in range(len(stations)):
            [x, fuel_at_station] = stations[i]

            elementsToAdd = []

            while heap and -heap[0][0] >= x:
                elem = heappop(heap)
                elementsToAdd.append(elem)
                new_x = ((-elem[0]) - x) + fuel_at_station + x
                moves = elem[1] + 1
                if new_x >= target:
                    ans = min(moves, ans)
                else:
                    elementsToAdd.append((-new_x, moves))
            for elem in elementsToAdd:
                heappush(heap, elem)

        return -1 if ans == float('inf') else ans


sol = Solution()
print(sol.minRefuelStops(1000,
                         246,
                         [[12, 86], [49, 157], [82, 18], [111, 137], [179, 168], [277, 80], [308, 81], [309, 185],
                          [340, 32], [347, 128], [415, 100], [521, 101], [554, 128], [558, 116], [580, 135], [602, 50],
                          [618, 152], [638, 90], [714, 51], [785, 33], [802, 151], [821, 185], [870, 175], [890, 158],
                          [916, 193]]))
