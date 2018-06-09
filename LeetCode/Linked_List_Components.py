class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        d = {}
        i = 0
        temp = head
        while temp != None:
            d[temp.val] = i
            i += 1
            temp = temp.next

        l = []
        for j, elem in enumerate(G):
            l.append(d[elem])

        zipped = sorted(zip(l, G))
        ans = 0
        prev = -2
        for i in range(0, len(G)):
            if zipped[i][0] != prev + 1:
                ans += 1
            prev = zipped[i][0]
        return ans


sol = Solution()
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(0)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(3)
print(sol.numComponents(l, [3, 4, 0, 2, 1]))
