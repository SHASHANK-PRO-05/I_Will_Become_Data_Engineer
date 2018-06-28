class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        curRemain = p
        up = True
        east = True

        while True:
            curRemain = curRemain - q
            if curRemain == 0:
                if up:
                    if east:
                        return 1
                    else:
                        return 2
                else:
                    return 0
            if curRemain < 0:
                curRemain = curRemain + p
                up = not up
            east = not east


sol = Solution()
print(sol.mirrorReflection(6, 4))
