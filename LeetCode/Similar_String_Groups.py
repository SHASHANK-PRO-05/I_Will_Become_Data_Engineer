import itertools


class Solution:
    def numSimilarGroups(self, A):
        parents = {x: x for x in A}
        n, m = len(A), len(A[0])
        self.count = n

        def find(x):
            if x != parents[x]: parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                parents[x] = y
                self.count -= 1
                return True
            return False

        def similar(x, y):
            return sum(i != j for i, j in zip(x, y)) == 2

        ## Real Solution Part ##
        if n < m:
            for x, y in itertools.combinations(A, 2):
                if similar(x, y): union(x, y)
        else:
            for x in A:
                for i, j in itertools.combinations(range(m), 2):
                    y = x[:i] + x[j] + x[i + 1:j] + x[i] + x[j + 1:]
                    if y in parents: union(x, y)
        return self.count


sol = Solution()
print(sol.numSimilarGroups(["tars", "rats", "arts", "star"]))
