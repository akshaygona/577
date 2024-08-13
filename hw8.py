def knapsackProblem(items, numItems, weight, memo=None):
    if memo is None:
        memo = {}
    if (numItems, weight) in memo:
        return memo[(numItems, weight)]
    if numItems == 0 or weight == 0:
        return 0
    if items[numItems - 1][0] > weight:
        result = knapsackProblem(items, numItems - 1, weight, memo)
    else:
        included = items[numItems - 1][1] + knapsackProblem(items, numItems - 1, weight - items[numItems - 1][0], memo)
        not_included = knapsackProblem(items, numItems - 1, weight, memo)
        result = max(included, not_included)

    memo[(numItems, weight)] = result
    return result


numInstances = int(input())
lines = []
for i in range(numInstances):
    l = input().split(' ')
    numItems = int(l[0])
    weight = int(l[1])
    items = []
    for j in range(numItems):
        items.append([int(num) for num in input().split(' ')])
    lines.append(knapsackProblem(items, numItems, weight))
for line in lines:
    print(line)