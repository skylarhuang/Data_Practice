def lastOccur(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
    if len(array)==0:
        return -1

    left = 0
    right = len(array)-1

    while left < right-1:
        mid = (left+right)/2

        if array[mid] > target:
            right = mid
        else:
            left = mid

    if array[right]==target:
      return right
    if array[left]==target:
      return left
    return -1