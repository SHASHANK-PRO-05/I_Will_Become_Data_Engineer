class heap:
    def __init__(self, val, key):
        self.val = val
        self.key = key

    def __le__(self, other):
        if self.key > other.key:
            return True
        elif self.key == other.key and self.val < other.val:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.key < other.key:
            return True
        elif self.key == other.key and self.val > other.val:
            return True
        else:
            return False


class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        map = {}
        for word in words:
            if word not in map:
                map[word] = 1
            else:
                map[word] += 1

        array = []
        for i in map.items():
            array.append(heap(i[0], i[1]))

        array = sorted(array)
        ans = []
        for i in range(0, k):
            ans.append(array[i].val)
        return ans


sol = Solution()
print(sol.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],
                       2))
