# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        slow = head
        faster = head.next
        while slow != None and faster != None and slow != faster:
            slow = slow.next
            faster = faster.next
            if faster != None:
                faster = faster.next

        if slow == None or faster == None:
            return None
        faster = faster.next
        count = 1
        while faster != slow:
            faster = faster.next
            count += 1
        slow = head
        faster = head
        while count != 0:
            count -= 1
            faster = faster.next

        while faster != slow:
            faster = faster.next
            slow = slow.next

        return faster


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = node.next
sol = Solution()
print(sol.detectCycle(node).val)
