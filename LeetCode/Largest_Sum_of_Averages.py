class Solution:
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        if K == 1:
            return round(sum(A) / len(A), 6)
        if K == 2:
            raise self.maximizeHalves(A)
        indices = [i for i in range(0, len(A))]
        zipped = sorted(zip(A, indices), reverse=True)
        s = 0
        partitions = [(0, len(A) - 1)]
        for i in range(0, K - 2):
            s = zipped[i][0]

            for j, partition in enumerate(partitions):
                if partition[0] <= zipped[i][1] <= partition[1]:
                    if zipped[i][1] == partition[0]:
                        partitions = partitions[0:j] + [(partition[0], partition[0]),
                                                        (partition[0] + 1, partition[1])] + partitions[
                                                                                            j + 1:len(partitions)]
                    elif zipped[i][1] == partition[1]:
                        partitions = partitions[0:j] + [
                            (partition[0], partition[1] - 1), (partition[1], partition[1])] + partitions[
                                                                                              j + 1:len(partitions)]
                    else:
                        partitions = partitions[0:j] + [(partition[0], zipped[i][1] - 1), (zipped[i][1], zipped[i][1]),
                                                        (zipped[i][1] + 1, partition[1])] + partitions[
                                                                                            j + 1:len(partitions)]
                    continue

            print(partitions)

    def maximizeHalves(self, A):
        s = sum(A)
        m = -1.0
        tempSum = 0
        for i in range(0, len(A)):
            len1 = i + 1
            len2 = len(A) - i - 1
            tempSum += A[i]
            m = max(m, tempSum / len1 + (s - tempSum) / len2)
        return m


sol = Solution()
sol.largestSumOfAverages([9, 1, 2, 3, 9], 3)
