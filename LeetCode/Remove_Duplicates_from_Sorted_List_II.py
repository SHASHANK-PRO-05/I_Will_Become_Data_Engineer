# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, newHead):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if newHead == None:
            return None
        iter = newHead
        head = None
        curVal = None
        end = head
        processThis = True
        while iter != None:
            if curVal == None:
                curVal = iter.val
            elif curVal == iter.val:
                processThis = False
            elif curVal != iter.val:
                if processThis:
                    node = ListNode(curVal)
                    if head == None:
                        head = node
                        end = node
                    else:
                        end.next = node
                        end = node
                curVal = iter.val
                processThis = True
            iter = iter.next
        if processThis:
            node = ListNode(curVal)
            if head == None:
                head = node
                end = node
            else:
                end.next = node
                end = node
        return head


sol = Solution()
n = ListNode(1)
n.next = ListNode(2)
n.next.next = ListNode(3)
n.next.next.next = ListNode(3)
n.next.next.next.next = ListNode(4)
n.next.next.next.next.next = ListNode(4)
n.next.next.next.next.next.next = ListNode(5)
temp = sol.deleteDuplicates(n)
print(temp)
