# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import *


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        def keyCheck(elem):
            return elem.val

        heap = []
        for i in range(0, len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i, lists[i]))
        head, end = None, None
        while heap:
            elem = heappop(heap)
            if elem[2].next:
                heappush((elem[2].next.val, elem[1], elem[2].next))
            if not head:
                head = elem
                end = elem
            else:
                end.next = elem
                end = elem
            elem.next = None
        return head
