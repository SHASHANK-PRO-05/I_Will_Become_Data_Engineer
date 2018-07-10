class Solution:
    # def shoppingOffers(self, price, special, needs):
    #     """
    #     :type price: List[int]
    #     :type special: List[List[int]]
    #     :type needs: List[int]
    #     :rtype: int
    #     """
    #     zeros = [0] * len(price)
    #     for i in range(0, len(price)):
    #         special.append(zeros[0:i] + [1] + zeros[i + 1:] + [price[i]])
    #
    #     memo = {tuple(zeros): 0}
    #
    #     def recursive(array):
    #         t = tuple(array)
    #         if t in memo:
    #             return memo[t]
    #         for offer in special:
    #             newArray = subtract(array, offer)
    #             if min(newArray) >= 0:
    #                 temp_ans = recursive(newArray)
    #                 if t in memo:
    #                     memo[t] = min(temp_ans + offer[-1], memo[t])
    #                 else:
    #                     memo[t] = temp_ans + offer[-1]
    #         return memo[t]
    #
    #     return recursive(needs)
    def shoppingOffers(self, price, special, needs):
        d = {}

        def dfs(cur):
            val = sum(cur[i] * price[i] for i in range(len(needs)))  # cost without special
            for spec in special:
                tmp = [cur[j] - spec[j] for j in range(len(needs))]
                if min(tmp) >= 0:  # skip deals that exceed needs
                    val = min(val, d.get(tuple(tmp), dfs(tmp)) + spec[
                        -1])  # .get check the dictionary first for result, otherwise perform dfs.
            d[tuple(cur)] = val
            return val

        return dfs(needs)


def listGreater(array1, array2):
    for i in range(0, len(array1)):
        if array1[i] < array2[i]:
            return False
    return True


def subtract(array1, array2):
    array = [array1[j] - array2[j] for j in range(len(array1))]
    return array


def addition(array1, array2):
    for i in range(0, len(array1)):
        array1[i] += array2[i]
    return array1


sol = Solution()
print(sol.shoppingOffers([9, 6, 1, 5, 3, 4],
                         [[1, 2, 2, 1, 0, 4, 14], [6, 3, 4, 0, 0, 1, 16], [4, 5, 6, 6, 2, 4, 26],
                          [1, 1, 4, 3, 4, 3, 15], [4, 2, 5, 4, 4, 5, 15], [4, 0, 0, 2, 3, 5, 13], [2, 4, 6, 4, 3, 5, 7],
                          [3, 3, 4, 2, 2, 6, 21], [0, 3, 0, 2, 3, 3, 15], [0, 2, 4, 2, 2, 5, 24],
                          [4, 1, 5, 4, 5, 4, 25], [6, 0, 5, 0, 1, 1, 14], [4, 0, 5, 2, 1, 5, 8], [4, 1, 4, 4, 3, 1, 10],
                          [4, 4, 2, 1, 5, 0, 14], [2, 4, 4, 1, 3, 1, 16], [4, 2, 3, 1, 2, 1, 26], [2, 4, 1, 6, 5, 3, 2],
                          [0, 2, 0, 4, 0, 0, 19], [3, 1, 6, 3, 3, 1, 23], [6, 2, 3, 2, 4, 4, 16], [5, 3, 5, 5, 0, 4, 5],
                          [5, 0, 4, 3, 0, 2, 20], [5, 3, 1, 2, 2, 5, 8], [3, 0, 6, 1, 0, 2, 10], [5, 6, 6, 1, 0, 4, 12],
                          [0, 6, 6, 4, 6, 4, 21], [0, 4, 6, 5, 0, 0, 22], [0, 4, 2, 4, 4, 6, 16],
                          [4, 2, 1, 0, 6, 5, 14], [0, 1, 3, 5, 0, 3, 8], [5, 5, 3, 3, 2, 0, 4], [1, 0, 3, 6, 2, 3, 18],
                          [4, 2, 6, 2, 2, 5, 2], [0, 2, 5, 5, 3, 6, 12], [1, 0, 6, 6, 5, 0, 10], [6, 0, 0, 5, 5, 1, 24],
                          [1, 4, 6, 5, 6, 3, 19], [2, 2, 4, 2, 4, 2, 20], [5, 6, 1, 4, 0, 5, 3], [3, 3, 2, 2, 1, 0, 14],
                          [0, 1, 3, 6, 5, 0, 9], [5, 3, 6, 5, 3, 3, 11], [5, 3, 3, 1, 0, 2, 26], [0, 1, 1, 4, 2, 1, 16],
                          [4, 2, 3, 2, 1, 4, 6], [0, 2, 1, 3, 3, 5, 15], [5, 6, 4, 1, 2, 5, 18], [1, 0, 0, 1, 6, 1, 16],
                          [2, 0, 6, 6, 2, 2, 17], [4, 4, 0, 2, 4, 6, 12], [0, 5, 2, 5, 4, 6, 6], [5, 2, 1, 6, 2, 1, 24],
                          [2, 0, 2, 2, 0, 1, 14], [1, 1, 0, 5, 3, 5, 16], [0, 2, 3, 5, 5, 5, 6], [3, 2, 0, 6, 4, 6, 8],
                          [4, 0, 1, 4, 5, 1, 6], [5, 0, 5, 6, 6, 3, 7], [2, 6, 0, 0, 2, 1, 25], [0, 4, 6, 1, 4, 4, 6],
                          [6, 3, 1, 4, 1, 1, 24], [6, 2, 1, 2, 1, 4, 4], [0, 1, 2, 3, 0, 1, 3], [0, 2, 5, 6, 5, 2, 13],
                          [2, 6, 4, 2, 2, 3, 17], [3, 4, 5, 0, 5, 4, 20], [6, 2, 3, 4, 1, 3, 4], [6, 4, 0, 0, 0, 5, 16],
                          [3, 1, 2, 5, 0, 6, 11], [1, 3, 2, 2, 5, 6, 14], [1, 3, 4, 5, 3, 5, 18], [2, 1, 1, 2, 6, 1, 1],
                          [4, 0, 4, 0, 6, 6, 8], [4, 6, 0, 5, 0, 2, 1], [3, 1, 0, 5, 3, 2, 26], [4, 0, 4, 0, 6, 6, 6],
                          [5, 0, 0, 0, 0, 4, 26], [4, 3, 2, 2, 0, 2, 14], [5, 2, 4, 0, 2, 2, 26],
                          [3, 4, 6, 0, 2, 4, 25], [2, 1, 5, 5, 1, 3, 26], [0, 5, 2, 4, 0, 2, 24], [5, 2, 5, 4, 5, 0, 1],
                          [5, 3, 0, 1, 5, 4, 15], [6, 1, 5, 1, 2, 1, 21], [2, 5, 1, 2, 1, 4, 15], [1, 4, 4, 0, 0, 0, 1],
                          [5, 0, 6, 1, 1, 4, 22], [0, 1, 1, 6, 1, 4, 1], [1, 6, 0, 3, 2, 2, 17], [3, 4, 3, 3, 1, 5, 17],
                          [1, 5, 5, 4, 5, 2, 27], [0, 6, 5, 5, 0, 0, 26], [1, 4, 0, 3, 1, 0, 13], [1, 0, 3, 5, 2, 4, 5],
                          [2, 2, 2, 3, 0, 0, 11], [3, 2, 2, 1, 1, 1, 6], [6, 6, 1, 1, 1, 6, 26],
                          [1, 5, 1, 2, 5, 2, 12]],
                         [6, 6, 6, 1, 6, 6]))
