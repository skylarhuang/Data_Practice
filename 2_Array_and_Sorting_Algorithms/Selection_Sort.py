def solve(array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    if len(array) == 1 or len(array) == 0:
        return array
    for i in range(len(array)):
        largest_index = 0
        for j in range(len(array) - i):
            if array[j] >= array[largest_index]:
                largest_index = j
        array[largest_index], array[len(array) - i - 1] = array[len(array) - i - 1], array[largest_index]
    return array