from heapq import *


class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        array = [(None, None, None)] * len(buildings) * 2
        for i in range(0, len(array), 2):
            index = int(i / 2)
            array[i] = (buildings[index][0], -buildings[index][2], buildings[index][1])
            array[i + 1] = (buildings[index][1], buildings[index][2], buildings[index][0])

        array = sorted(array)

        ans = []
        heap = []
        for elem in array:
            if elem[1] < 0:
                heappush(heap, (elem[1], elem[2]))
                if len(ans) != 0 and ans[-1][0] == elem[0]:
                    ans[-1][1] = max(ans[-1][1], -elem[1])
                elif len(ans) == 0 or ans[-1][1] < -elem[1]:
                    ans.append([elem[0], -elem[1]])
            else:
                if heap:
                    if -heap[0][0] == elem[1] and heap[0][1] == elem[0]:
                        newPeek = heap[0]
                        while newPeek[1] <= elem[0] and heap:
                            heappop(heap)
                            if heap:
                                newPeek = heap[0]
                        if not heap:
                            ans.append([elem[0], 0])
                        elif -newPeek[0] != elem[1]:
                            ans.append([elem[0], -newPeek[0]])

        return ans


sol = Solution()
print(sol.getSkyline([[0, 2, 3], [2, 5, 3]]))
