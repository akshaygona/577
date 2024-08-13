def mergeCount(a, b):
    S = []
    c = 0
    i = j = 0
    len_a = len(a)
    len_b = len(b)

    while i < len_a or j < len_b:
        a0 = a[i] if i < len_a else float('inf')
        b0 = b[j] if j < len_b else float('inf')

        if a0 <= b0:
            S.append(a0)
            i += 1
        else:
            S.append(b0)
            c += len_a - i
            j += 1
    return S, c


def countSort(array):
    size = len(array)
    if size == 1:
        return array, 0
    half = size // 2
    a1, c1 = countSort(array[:half])
    a2, c2 = countSort(array[half:])
    a, c = mergeCount(a1, a2)
    return a, c + c1 + c2


numInstances = int(input())
output = []

for _ in range(numInstances):
    n = int(input())
    p = []
    q = []

    for _ in range(n):
        p.append(int(input()))
    for _ in range(n):
        q.append(int(input()))

    sorted_indices = sorted(range(n), key=lambda k: p[k])
    sorted_q = [q[i] for i in sorted_indices]

    _, count = countSort(sorted_q)
    output.append(str(count))

print('\n'.join(output))
