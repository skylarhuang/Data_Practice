def twoDbinary(nums, target):
  if nums is None or len(nums) == 0:
    return None

  N, M = len(nums), len(nums[0])
  left, right = 0, N*M
  while left <= right:
    mid = (left + right)/2
    row_num = mid / M
    col_num = mid / N
    if nums[row_num][col_num] == target:
      return row_num, col_num
    elif nums[row_num][col_num] < target:
      left = mid + 1
    else:
      right = mid - 1
  
  return None


x = [[1,4,7], [8,11,12], [15,16,18], [21,26,30]]

print(twoDbinary(x, 30))