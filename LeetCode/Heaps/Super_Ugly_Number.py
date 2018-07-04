import heapq


class Solution:
    def UnoptimzednthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        heap = [1]
        visited = {1: True}
        for i in range(1, n + 1):
            elem = heapq.heappop(heap)
            if i == n:
                return elem
            for p in primes:
                if not visited[p * elem]:
                    heapq.heappush(heap, p * elem)
                    visited[p * elem] = True

    def nthSuperUglyNumber(self, n, primes):
        uglies = [1]

        def gen(prime):
            for ugly in uglies:
                yield ugly * prime

        merged = heapq.merge(*map(gen, primes))
        while len(uglies) < n:
            ugly = next(merged)
            if ugly != uglies[-1]:
                uglies.append(ugly)
        return uglies[-1]


sol = Solution()
print(sol.nthSuperUglyNumber(12,
                             [2, 7, 13, 19]))
