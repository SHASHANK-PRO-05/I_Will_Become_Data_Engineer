class LinkedList:
    def __init__(self, list):
        self.list = list
        self.counter = list[1]
        self.next = None

    def __gt__(self, other):
        if self.list[0] != other.list[0]:
            return self.list[0] < other.list[0]
        else:
            return self.list[1] > other.list[1]

    def __lt__(self, other):
        if self.list[0] != other.list[0]:
            return self.list[0] > other.list[0]
        else:
            return self.list[1] < other.list[1]


class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        array = [None] * len(people)
        for i in range(0, len(people)):
            array[i] = LinkedList(people[i])
        array = sorted(array)
        head = None
        for i in range(0, len(array)):
            if head == None:
                head = array[i]
            else:
                temp = head
                prev = None
                

sol = Solution()
print(sol.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
