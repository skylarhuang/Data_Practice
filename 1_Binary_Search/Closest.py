def FindNearest(array, target):
  if len(array) == 0 or not array:
    return None
  
  left, right = 0, len(array)-1
  while left < right - 1:
    mid = (right + left) /2
    if array[mid] == target:
      return mid
    elif array[mid] < target:
      left = mid
    else:
      right = mid

  return left if (abs(array[left]-target) < abs(array[right]-target)) else right


x = [1,3,4,7,8,9,11,13]

print(FindNearest(x,6))