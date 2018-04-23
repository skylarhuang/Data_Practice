def totalOccurrence(array, target):
  if len(array) == 0:
    return 0
  else:
    firstoccur = firstOccur(array,target)
    lastoccur = lastOccur(array,target)
    if (firstoccur==-1) and (lastoccur==-1):
      return 0
    else:
      return (lastoccur-firstoccur+1)
      
def firstOccur(array, target):  
  left = 0
  right = len(array)-1
  
  while (left < right-1):
    mid = int((left+right)/2)
    if array[mid] < target:
      left = mid  
    elif array[mid]>=target:
      right = mid
  if array[left]==target:
    return left
  if array[right]==target:
    return right
  return -1
    
def lastOccur(array, target):
  left = 0
  right = len(array)-1
  
  while (left < right-1):
    mid = int((left+right)/2)
    if array[mid] <= target:
      left = mid  
    elif array[mid]>target:
      right = mid
  if array[right]==target:
    return right
  if array[left]==target:
    return left
  return -1
    
array1 = [1, 2, 2, 3, 3, 3, 3, 4, 5, 5]
print(totalOccurrence(array1,3))