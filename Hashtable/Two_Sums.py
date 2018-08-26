def two_sum(nums, target):
  if len(nums)<=1:
    return False
  my_dic = {}
  for i in range(len(nums)):
    if nums[i] in my_dic:
      return {my_dic[nums[i]],i}
    else:
      my_dic[target-nums[i]] = i

nums = [1,2,3,4,5]
target = 6

print(two_sum(nums,target))