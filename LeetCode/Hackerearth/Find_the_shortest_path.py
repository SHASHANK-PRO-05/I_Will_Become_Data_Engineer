def simulation():
    n = int(input())
    parents = []
    for i in range(0, n):
        for j in range(i + 1, n):
            print(i, j)


simulation()
