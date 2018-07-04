def bruteForceSimulation():
    n = int(input())
    array = list(map(lambda x: int(x), input().split(' ')))
    visited = [False] * len(array)
    possibleSolutions = []

    def check(l):
        if len(l) == n:
            if sorted(l) not in possibleSolutions:
                possibleSolutions.append(sorted(l))
                print(sorted(l))

        for i in range(0, len(array)):
            if not visited[i]:
                visited[i] = True
                for j in range(i + 1, len(array)):
                    if not visited[j]:
                        visited[j] = True
                        check(l + [(array[i], array[j])])
                        visited[j] = False
                visited[i] = False

    check([])
    ans = 0

    for i in range(0, len(possibleSolutions)):
        s = set([])
        for j in range(0, n):
            for k in range(possibleSolutions[i][j][0], possibleSolutions[i][j][1]):
                s.add(k)
        # print(i, possibleSolutions[i], s)
        ans += len(s)

    print(len(possibleSolutions))
    print(ans)


def dynamicSimulation():
    n = int(input())
    mod = 10 ** 9 + 7

    array = list(map(lambda x: int(x) % mod, input().split(' ')))
    diff = array[-1] - array[0]

    d = [0] * (n + 1)
    d[0] = 1
    d[1] = 1
    for i in range(2, n + 1):
        odd = i * 2 - 1
        d[i] = (d[i - 1] * odd) % mod

    ans = d[n]
    ans = (ans * diff) % mod

    for i in range(2, 2 * n, 2):
        left = int(i / 2)
        right = int((2 * n - i) / 2)
        permutes = (d[left] * d[right]) % mod
        permutes = (permutes * (array[i] - array[i - 1])) % mod
        ans = ((ans - permutes) + mod) % mod

    print(ans)


dynamicSimulation()
# bruteForceSimulation()
