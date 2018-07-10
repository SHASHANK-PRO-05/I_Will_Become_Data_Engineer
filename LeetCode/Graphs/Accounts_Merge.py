from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        emailToName = {}
        union_find = {}
        emailList = defaultdict(lambda: [])

        def find_parent(email):
        
            if email not in union_find:
                union_find[email] = email
                return email
            if union_find[email] == email:
                return email
            union_find[email] = find_parent(union_find[email])
            return union_find[email]

        for i in range(0, len(accounts)):
            element = accounts[i]
            name = element[0]
            emailToName[element[1]] = name
            thisParent = find_parent(element[1])
            for j in range(2, len(element)):
                nextParent = find_parent(element[j])
                union_find[nextParent] = thisParent

        for key in union_find.keys():
            emailList[find_parent(key)].append(key)

        ans = []

        for key in emailList.keys():
            ans.append([emailToName[key]] + sorted(emailList[key]))
        return ans


sol = Solution()
print(sol.accountsMerge(
    [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"],
     ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]))
