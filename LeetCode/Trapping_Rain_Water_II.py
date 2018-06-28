import heapq


class Solution:
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if len(heightMap) < 2:
            return 0
        if len(heightMap[0]) < 2:
            return 0
        visited = []
        heap = []
        for i in range(0, len(heightMap)):
            visited.append([False] * len(heightMap[0]))
        ans = 0

        for i in range(0, len(heightMap[0])):
            heapq.heappush(heap, (heightMap[0][i], 0, i))
            visited[0][i] = True
            heapq.heappush(heap, (heightMap[len(heightMap) - 1][i], len(heightMap) - 1, i))
            visited[len(heightMap) - 1][i] = True

        for i in range(0, len(heightMap)):
            if not visited[i][0]:
                heapq.heappush(heap, (heightMap[i][0], i, 0))
                visited[i][0] = True
            if not visited[i][len(heightMap[0]) - 1]:
                heapq.heappush(heap, (heightMap[i][len(heightMap[0]) - 1], i, len(heightMap[0]) - 1))
                visited[i][len(heightMap[0]) - 1] = True
        upperLimit, lowerLimit, leftLimit, rightLimit = 0, len(heightMap) - 1, 0, len(heightMap[0]) - 1
        while heap:

            elem = heapq.heappop(heap)

            # go top
            if elem[1] - 1 > upperLimit and not visited[elem[1] - 1][elem[2]]:
                if heightMap[elem[1] - 1][elem[2]] < elem[0]:
                    ans += (elem[0] - heightMap[elem[1] - 1][elem[2]])
                    heapq.heappush(heap, (elem[0], elem[1] - 1, elem[2]))
                else:
                    heapq.heappush(heap, (heightMap[elem[1] - 1][elem[2]], elem[1] - 1, elem[2]))
                visited[elem[1] - 1][elem[2]] = True

            if elem[1] + 1 < lowerLimit and not visited[elem[1] + 1][elem[2]]:
                if heightMap[elem[1] + 1][elem[2]] < elem[0]:
                    ans += (elem[0] - heightMap[elem[1] + 1][elem[2]])
                    heapq.heappush(heap, (elem[0], elem[1] + 1, elem[2]))
                else:
                    heapq.heappush(heap, (heightMap[elem[1] + 1][elem[2]], elem[1] + 1, elem[2]))
                visited[elem[1] + 1][elem[2]] = True

            if elem[2] + 1 < rightLimit and not visited[elem[1]][elem[2] + 1]:
                if heightMap[elem[1]][elem[2] + 1] < elem[0]:
                    ans += (elem[0] - heightMap[elem[1]][elem[2] + 1])
                    heapq.heappush(heap, (elem[0], elem[1], elem[2] + 1))
                else:
                    heapq.heappush(heap, (heightMap[elem[1]][elem[2] + 1], elem[1], elem[2] + 1))
                visited[elem[1]][elem[2] + 1] = True

            if elem[2] - 1 > leftLimit and not visited[elem[1]][elem[2] - 1]:
                if heightMap[elem[1]][elem[2] - 1] < elem[0]:
                    ans += (elem[0] - heightMap[elem[1]][elem[2] - 1])
                    heapq.heappush(heap, (elem[0], elem[1], elem[2] - 1))
                else:
                    heapq.heappush(heap, (heightMap[elem[1]][elem[2] - 1], elem[1], elem[2] - 1))
                visited[elem[1]][elem[2] - 1] = True

        return ans


sol = Solution()
print(sol.trapRainWater([[12, 13, 1, 12], [13, 4, 13, 12], [13, 8, 10, 12], [12, 13, 12, 12], [13, 13, 13, 13]]))
