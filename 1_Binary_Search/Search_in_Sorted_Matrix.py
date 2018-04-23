def search(matrix, target):
    """
    input: int[][] matrix, int target
    return: int[]
    """
    # write your solution here
    M = len(matrix[0])
    N = len(matrix)
    left = 0
    right = M * N - 1

    while left <= right:
        mid = (left + right) / 2
        row = int(mid // M)
        col = int(mid % M)

        if matrix[row][col] > target:
            right = mid - 1
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            return ([row, col])

    return ([-1, -1])