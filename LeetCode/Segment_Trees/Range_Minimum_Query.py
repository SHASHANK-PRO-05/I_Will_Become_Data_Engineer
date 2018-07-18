import math

# https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/tutorial/

[n, q] = list(map(int, input().split(' ')))
array = list(map(int, input().split(' ')))
x = int(math.ceil(math.log2(n)))
tree = [0] * (2 * (2 ** x) - 1)


def build(node, start, end):
    if start == end:
        tree[node] = array[start]
        return array[start]
    else:
        mid = int((start + end) / 2)
        currentMin = build(node * 2 + 1, start, mid)
        currentMin = min(currentMin, build(node * 2 + 2, mid + 1, end))
        tree[node] = currentMin
        return currentMin


build(0, 0, n - 1)


def query(node, start, end, l, r):
    if r < start or end < l:
        return float('inf')
    if l <= start and end <= r:
        return tree[node]
    mid = int((start + end) / 2)
    currMin = query(node * 2 + 1, start, mid, l, r)
    currMin = min(currMin, query(node * 2 + 2, mid + 1, end, l, r))
    return currMin


def update(node, start, end, index, value):
    if start == end:
        array[index] = value
        tree[node] = value
    else:
        mid = int((start + end) / 2)
        if start <= index and index <= mid:
            update(node * 2 + 1, start, mid, index, value)
        else:
            update(node * 2 + 2, mid + 1, end, index, value)
        tree[node] = min(tree[node * 2 + 1], tree[node * 2 + 2])


for i in range(q):
    check = input().split(' ')
    if check[0] == 'u':
        update(0, 0, n - 1, int(check[1]) - 1, int(check[2]))
    else:
        print(query(0, 0, n - 1, int(check[1]) - 1, int(check[2]) - 1))
