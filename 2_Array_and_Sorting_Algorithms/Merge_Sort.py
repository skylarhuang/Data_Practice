def mergeSort(array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here

    if len(array) == 0 or len(array) == 1:
        return array
    else:
        mid = len(array) // 2
        a = self.mergeSort(array[:mid])
        b = self.mergeSort(array[mid:])
        return self.merge(a, b)


def merge(a, b):
    c = []
    index_a = index_b = 0
    while index_a < len(a) and index_b < len(b):
        if a[index_a] < b[index_b]:
            c.append(a[index_a])
            index_a = index_a + 1
        else:
            c.append(b[index_b])
            index_b = index_b + 1
    if index_a < len(a):
        c.extend(a[index_a:])
    if index_b < len(b):
        c.extend(b[index_b:])
    return c