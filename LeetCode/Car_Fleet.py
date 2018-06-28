import math


class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """

        n_cars = len(position)
        if n_cars == 0:
            return 0
        zipped = []

        def keyCheck(elem):
            return elem[0]

        for i in range(0, n_cars):
            zipped.append([(position[i], speed[i], 0)])
        zipped = sorted(zipped, reverse=True, key=keyCheck)

        fleet = 1

        for i in range(1, n_cars):
            next_car = zipped[i - 1]
            this_car = zipped[i][0]
            process = True
            for iter, elem in enumerate(next_car):
                if elem[1] < this_car[1]:
                    speedDiff = this_car[1] - elem[1]
                    distDiff = elem[0] - this_car[0] - (elem[2] * this_car[1])
                    if distDiff < 0:
                        distDiff = 0
                    meetingPoint = (distDiff / speedDiff) * elem[1] + elem[0]
                    if meetingPoint <= target:
                        process = False
                        zipped[i].append((meetingPoint, elem[1], elem[2] + (distDiff / speedDiff)))
            if process:
                fleet += 1
        # print(zipped)
        return fleet


sol = Solution()
print(sol.carFleet(21,
                   [1, 15, 6, 8, 18, 14, 16, 2, 19, 17, 3, 20, 5],
                   [8, 5, 5, 7, 10, 10, 7, 9, 3, 4, 4, 10, 2]))
