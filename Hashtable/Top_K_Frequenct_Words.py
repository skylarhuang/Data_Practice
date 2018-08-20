combo = ["a", "a", "b", "b", "b", "b", "c", "c", "c", "d"]


def topKFrequent(combo, k):
    myDict = {}
    for word in combo:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1

    print(myDict)

    key = []
    value = []
    result = []

    for ky, v in myDict.items():
        key.append(ky)
        value.append(-1 * v)

    top_k = sorted(range(len(value)), key=lambda i: value[i])[:k]

    for t in top_k:
        result.append(key[t])
    return result


print(topKFrequent(combo, 2))