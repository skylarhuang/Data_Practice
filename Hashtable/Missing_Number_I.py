array1 = [12, 11, 10, 9, 4, 5, 6, 7, 2, 3, 8]

def missing(array):
    myDict = {}
    for i in range(len(array) + 1):
        myDict[i + 1] = 0

    for number in array:
        if number in myDict:
            myDict[number] += 1

    for k, v in myDict.items():
        if v == 0:
            miss = k
    return miss

x = missing(array1)
print(x)

# Answer is 1
