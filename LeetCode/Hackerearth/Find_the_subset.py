[n, m, d] = map(lambda x: int(x), input().split(' '))

set = sorted([(elem, i) for i, elem in enumerate(map(lambda x: int(x), input().split(' ')))])

set = [i[1] for i in sorted(map(lambda x: (x[1], x[0]), set[0:n]))]

print(''.join(str(x) for x in set))
