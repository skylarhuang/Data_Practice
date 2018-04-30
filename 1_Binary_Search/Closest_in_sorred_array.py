def closest(array, target):
  if len(array)==0 or not array:
    return -1
  left = 0
  right = len(array)-1
    
  while left<right-1:
    mid = (left+right)//2
    if target < array[mid]:
      right = mid
    elif target > array[mid]:
      left = mid
    else:
      return mid
  return left if abs(array[left]-target)<abs(array[right]-target) else right