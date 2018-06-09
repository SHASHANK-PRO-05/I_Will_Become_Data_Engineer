class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.d = dict()
        self.head = None
        self.end = None
        self.currLen = 0
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.d.keys():
            return -1
        elem = self.d[key]

        ans = elem.val

        if elem == self.head:
            return ans
        elif elem == self.end:
            self.end = self.end.prev
            self.end.next = None
            elem.next = self.head
            elem.prev = None
            self.head.prev = elem
            self.head = elem
        else:
            elem.next.prev = elem.prev
            elem.prev.next = elem.next
            elem.prev = None
            elem.next = self.head
            self.head.prev = elem
            self.head = elem
        return ans

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        v = self.get(key)
        if v != -1:
            self.d[key].val = value
            return
        elif self.currLen < self.capacity:
            node = Node(value, key)
            if self.head == None:
                self.head = node
                self.end = node
            else:
                node.next = self.head
                self.head.prev = node
                self.head = node
            self.currLen += 1
            self.d[key] = node
        else:
            node = Node(value, key)
            if self.capacity == 1:
                self.d[key] = node
                del self.d[self.head.key]
                self.head = node
                self.end = node
            else:
                del self.d[self.end.key]
                elem = self.end
                self.end = self.end.prev
                elem.prev = None
                self.end.next = None
                node.next = self.head
                self.head.prev = node
                self.head = node
            self.d[key] = node


cache = LRUCache(3)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
