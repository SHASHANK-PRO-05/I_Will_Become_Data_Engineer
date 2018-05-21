class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if len(S) == 0:
            return []
        maxElem = [-1] * 26
        for i in range(0, len(S)):
            maxElem[ord(S[i]) - 97] = i

        currStar = 0
        ansList = []
        currEnd = maxElem[ord(S[0]) - 97]
        for i in range(1, len(S)):
            if currEnd < i:
                ansList.append(currEnd - currStar + 1)
                currStar = i
                currEnd = maxElem[ord(S[i]) - 97]
            elif currEnd >= i:
                currEnd = max(currEnd, maxElem[ord(S[i]) - 97])
        ansList.append(currEnd - currStar + 1)
        return ansList


if __name__ == "__main__":
    sol = Solution()
    print(sol.partitionLabels('ababcbacadefegdehijhklij'))
