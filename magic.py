import heapq

def magic(k, stream):
    heap = []
    for number in stream:
        heapq.heappush(heap, number)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap

stream = [10, 1, 5, 2, 3, 9, 4, 6, 8, 7]
print(magic(3, stream))