class Solution(object):
  def closest (self, array, target):
    if len(array) == 0 or not array:
      return []
    
    left, right = 0, len(array)-1
    while left < right - 1:
      mid = (left + right)/2
      if array[mid] == target:
        return mid
      elif array[mid] < target:
        left = mid
      else:
        right = mid
    return left if (abs(array[left]-target)<abs(array[right]-target)) else right
  
  def kClosest(self, array, target, k):
    """
    input: int[] array, int target, int k
    return: int[]
    """
    # write your solution here
    if len(array) == 0 or not array or k==0:
      return []
    
    res = []
    close = self.closest(array, target)
    res.append(array[close])
    left, right = close-1, close+1
    
    while len(res) < k:
      if left < 0:
        while right <= len(array)-1 and len(res)<k:
          res.append(array[right])
          right += 1
      elif right > len(array)-1 and len(res)<k:
        while left >= 0:
          res.append(array[left])
          left -= 1
      else:
        if abs(array[left]-target) <= abs(array[right]-target):
          res.append(array[left])
          left -= 1
        else:
          res.append(array[right])
          right += 1
    return res