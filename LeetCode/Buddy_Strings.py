class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A != B:
            currentDiff = 0
            curA, curB = None, None
            for i in range(0, len(A)):
                if A[i] != B[i]:
                    currentDiff += 1
                    if currentDiff == 1:
                        curA = A[i]
                        curB = B[i]
                    elif currentDiff == 2:
                        if A[i] == curB and B[i] == curA:
                            continue
                        else:
                            return False
                    else:
                        return False
            if currentDiff == 2:
                return True
            else:
                return False
        else:
            arr = [0] * 26
            for i in range(0, len(A)):
                arr[ord(A[i]) - ord('a')] += 1
                if arr[ord(A[i]) - ord('a')] >= 2:
                    return True
            return False


sol = Solution()
print(sol.buddyStrings("aacb", "caba"))
