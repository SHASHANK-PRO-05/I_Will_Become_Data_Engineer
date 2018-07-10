class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        union_find_mapping = {}
        ans_list = set()

        def union_find(node):
            if node not in union_find_mapping:
                union_find_mapping[node] = node
            elif union_find_mapping[node] != node:
                union_find_mapping[node] = union_find(union_find_mapping[node])
            return union_find_mapping[node]

        for i in range(len(M)):
            for j in range(len(M[i])):
                if not M[i][j] == 0:
                    parent = union_find(i)
                    child = union_find(j)
                    union_find_mapping[child] = parent
        for i in range(len(M)):
            ans_list.add(union_find(i))
        return len(ans_list)
