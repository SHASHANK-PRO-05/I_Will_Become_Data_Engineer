def bruteForceSimulation():
    [n, k] = list(map(lambda x: int(x), input().split(" ")))
    array = list(map(lambda x: int(x), input().split(" ")))
    s = sum(array)
    possibleSolutions = []
    mod = 10 ** 9 + 7

    def check(l):
        if len(l) == n:
            possibleSolutions.append(l)
            return
        for i in range(1, k + 1):
            check(l + [i])

    remainder = modPow(s, n, mod)

    multiplicationFactor = modPow(remainder, mod - 2, mod)

    check([])

    ans = 0
    d = {1: 0, 2: 0, 3: 0, 4: 0}
    for i in range(0, len(possibleSolutions)):
        tempAns = 1
        if scoring(possibleSolutions[i]) in d:
            d[scoring(possibleSolutions[i])] += 1
        else:
            d[scoring(possibleSolutions[i])] = 1
        print(possibleSolutions[i], scoring(possibleSolutions[i]))
        for j in range(0, n):
            tempAns = (tempAns * array[possibleSolutions[i][j] - 1]) % mod
        tempAns = (tempAns * scoring(possibleSolutions[i])) % mod
        ans = (ans + tempAns) % mod
    print(d)
    ans = (ans * multiplicationFactor) % mod
    print(ans)


def modPow(mantisa, pow, mod):
    ans = 1

    while pow != 0:
        if pow % 2 != 0:
            ans = (ans * mantisa) % mod
        pow = int(pow / 2)
        mantisa = (mantisa * mantisa) % mod
    return ans


def scoring(array):
    score = 1
    maxScore = 1
    array_ans = [1] * len(array)
    for i in range(len(array) - 2, -1, -1):
        for j in range(i + 1, len(array)):
            if array[j] >= array[i]:
                array_ans[i] = array_ans[j] + 1
                break

    for i in range(1, len(array)):
        if array[i] >= array[0]:
            maxScore = max(array_ans[i] + 1, maxScore)
            break
    return maxScore


bruteForceSimulation()
