# Definition for a unknown sized dictionary.
# class Dictionary(object):
#   def get(self, index):
#     pass

class Solution(object):
  def search(self, dic, target):
    """
    input: Dictionary dic, int target
    return: int
    """
    # write your solution here
    right = 1
    while dic.get(right) and dic.get(right)<target:
      right = right * 2
      
    left = 0
    # If want to return mid,  then the loop condition should be left<=right
    while left <= right:
      mid = (left+right)/2
      if target == dic.get(mid):
        return mid
      # Have to check if there is mid or not
      elif target < dic.get(mid) or not dic.get(mid):
        right = mid - 1
      else:
        left = mid + 1
        
    return -1
      