n = int(input())
ans = 0

array = list(map(lambda x: int(x), input().split(" ")))
ans += n + n - 1
queue = []

for i in range(0, len(array) - 1):
    queue.append((i, i + 1, [min(array[i], array[i + 1]), max(array[i], array[i + 1]), max(array[i], array[i + 1])]))
answers = []
while queue:
    elem = queue.pop()
    range = elem

    if range[1] == len(array) - 1:
        continue
    nextElem = array[range[1] + 1]
    min1 = range[2][0]
    min2 = range[2][1]
    MAX = range[2][2]

    # print(range, nextElem)
    if min1 + min2 >= nextElem and nextElem + min2 >= min1 and nextElem + min1 >= min2 and min1 + MAX >= nextElem and min1 + nextElem >= MAX and MAX + nextElem >= min1:

        ans += 1
        if min1 > nextElem:
            min2 = min1
            min1 = nextElem
        elif min2 > nextElem:
            min2 = nextElem
        answers.append((range[0], range[1] + 1, nextElem, min1, min2, max(nextElem, MAX)))
        queue.append((range[0], range[1] + 1, (min1, min2, max(nextElem, MAX))))

    # print(queue)

print(ans)
print(''.join(str(x) + "\n" for x in sorted(answers)))
