# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        iter = head
        d = dict()
        counter = 0
        l = []
        while iter != None:
            d[iter] = counter
            node = RandomListNode(iter.label)
            if counter != 0:
                l[len(l) - 1].next = node
            l.append(node)
            counter += 1
            iter = iter.next

        iter = head
        while iter != None:
            if iter.random != None:
                l[d[iter]].random = l[d[iter.random]]
            iter = iter.next
        return l[0]


node = RandomListNode(4)
