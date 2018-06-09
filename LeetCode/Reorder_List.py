# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None:
            return
        if head.next == None:
            return
        counter = 0
        reverse = None
        iter = head
        while iter != None:
            node = ListNode(iter.val)
            if reverse == None:
                reverse = node
            else:
                node.next = reverse
                reverse = node
            counter += 1
            iter = iter.next
        l = int(counter / 2)

        iter = head
        iter2 = reverse
        for i in range(0, l):
            elem = iter
            iter = iter.next
            elem.next = iter2
            iter2 = iter2.next
            if i != l - 1:
                elem.next.next = iter
            elif i == l - 1:
                if counter % 2 == 0:
                    elem.next.next = None
                else:
                    elem.next.next = iter
                    iter.next = None
