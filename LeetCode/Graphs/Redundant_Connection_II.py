class Solution:
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        union_find_dic = {}

        def find_parent(elem):
            if elem not in union_find_dic:
                union_find_dic[elem] = elem
            elif union_find_dic[elem] != elem:
                union_find_dic[elem] = find_parent(union_find_dic[elem])
            return union_find_dic[elem]

        ans = None
        for i in range(0, len(edges)):
            elem = edges[i]
            first = find_parent(elem[0])
            second = find_parent(elem[1])
            if first == second:
                ans = elem
            else:
                temp_min = min(first, second)
                union_find_dic[elem[0]] = temp_min
                union_find_dic[elem[1]] = temp_min
                
        return ans
