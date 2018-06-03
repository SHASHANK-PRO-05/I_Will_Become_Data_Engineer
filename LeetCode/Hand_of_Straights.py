import collections


class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        hand = sorted(list(collections.Counter(hand).items()))
        for i in range(0, len(hand)):
            if hand[i][1] != 0:

                if i + W > len(hand):
                    return False
                for j in range(i + 1, W + i):
                    if hand[j][0] != hand[j - 1][0] + 1:
                        return False
                    elif hand[j][1] < hand[i][1]:
                        return False
                    else:
                        hand[j] = (hand[j][0], hand[j][1] - hand[i][1])
                hand[i] = (hand[i][0], 0)
        return True


sol = Solution()
print(sol.isNStraightHand([8, 12, 4, 3, 11, 2, 1, 10, 1, 2, 3, 4, 5, 6, 7, 9], 3))
