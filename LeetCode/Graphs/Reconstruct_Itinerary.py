class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        ticket_dict = {}

        for i in range(0, len(tickets)):
            if tickets[i][0] in ticket_dict:
                ticket_dict[tickets[i][0]].append(tickets[i][1])
            else:
                ticket_dict[tickets[i][0]] = [tickets[i][1]]
        visited = {}    
        for key, row in ticket_dict.items():
            ticket_dict[key] = sorted(row)
            visited[key] = [False] * len(row)
        total_len = len(tickets)

        def dfs(node, curr_len):
            if curr_len == total_len:
                return [node]
            for i in range(0, len(ticket_dict[node])):
                if not visited[node][i]:
                    visited[node][i] = True
                    temp = dfs(ticket_dict[node][i], curr_len + 1)
                    if not temp == None:
                        return [node] + temp
                    else:
                        visited[node][i] = False
            return None

        return dfs('JFK', 0)


def testCase():
    sol = Solution()
    print(sol.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))


print(testCase())
