class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        ans = 0
        stack = []
        for i in range(0, len(S)):
            if S[i] == '(':
                stack.append(('(', 0))
            else:
                elem = stack.pop()
                tempAns = 0
                if elem[1] == 0:
                    tempAns = 1
                else:
                    tempAns = 2 * elem[1]
                if len(stack) == 0:
                    ans += tempAns
                else:
                    stack[-1] = (stack[-1][0], stack[-1][1] + tempAns)
        return ans


sol = Solution()
print(sol.scoreOfParentheses("()()"))
