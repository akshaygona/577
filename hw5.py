class InversionCounter:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def count_split(l, r):
    i = 0
    j = 0
    count = 0
    len_l = len(l)
    len_r = len(r)
    merged = []
    while i < len_l and j < len_r:
        if l[i] <= r[j]:
            merged.append(l[i])
            i += 1
        else:
            merged.append(r[j])
            j += 1
            count += len_l - i
    merged.extend(l[i:])
    merged.extend(r[j:])
    return count, merged


def count_inversions(numbers):
    count = len(numbers)
    if count == 0:
        return 0, numbers
    if count == 1:
        return 0, numbers
    else:
        left_half = numbers[:count // 2]
        left_count, left = count_inversions(left_half)
        right_half = numbers[count // 2:]
        right_count, right = count_inversions(right_half)
        merged_count, merged = count_split(left, right)
        answer = left_count + right_count + merged_count, merged
        return answer


num_instances = int(input())

for i in range(num_instances):
    answer = int(input())
    left = []
    right = []

    for j in range(answer):
        left.append(int(input()))

    for k in range(answer):
        right.append(int(input()))

    lines = list(zip(left, right))
    sorted_lines = sorted(lines, key=lambda points: points[0])
    finalist = [line[1] for line in sorted_lines]
    count, i = count_inversions(finalist)
    print(count)