def moveZeroes(self, nums):
  count = 0
    
  for i in range(len(nums)):
    if nums[i] != 0:
      nums[count] = nums[i]
      count = count + 1
    
  for j in range(count,len(nums)):
    nums[j] = 0
    
  return nums