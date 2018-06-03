class Solution:
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if '@' in S:
            return self.maskEmail(S)
        else:
            return self.maskPhone(S)

    def maskEmail(self, S):
        splits = S.split("@")
        ansString = splits[0][0].lower() + "*****" + splits[0][len(splits[0]) - 1].lower() + "@" + splits[1].lower()
        return ansString

    def maskPhone(self, S):
        digits = [x for x in S if x.isdigit()]
        ansList = []
        if len(digits) > 10:
            ansList += ['+'] + (['*'] * (len(digits) - 10)) + ['-']
        ansList += ['*'] * 3 + ['-'] + ['*'] * 3 + ['-']
        n = len(digits)
        ansList += digits[n - 4: n]
        return ''.join(x for x in ansList)


sol = Solution()
print(sol.maskPII("Leetcode@gmail.com"))
print(sol.maskPII("1(234)567-890"))
print(sol.maskPII('186-(10)12345678'))
