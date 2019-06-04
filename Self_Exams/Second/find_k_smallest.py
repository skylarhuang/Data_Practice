import heapq


def KSmallest(array, k):
    # Corner Case 1: empty array or k=0, return []
    if not array or k == 0:
        return []
    # Corner Case 2: k>length of array, return all of array
    if k > len(array):
        k = len(array)

    res = []
    heapq.heapify(array)

    for i in range(k):
        res.append(heapq.heappop(array))


    return res