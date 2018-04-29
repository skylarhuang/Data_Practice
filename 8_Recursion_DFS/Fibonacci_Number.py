def fibonacci( K):
  if K == 0 or K <= 0:
    return 0
  if K == 1:     
    return 1
  prev = 0
  curr = 1
  for i in range(K):
    prev, curr = curr, prev+curr
  return prev

def fibonacci( K):
  if K == 0 or K<=0:
    return 0
  if K == 1:
    return 1
  if K == 2:
    return 1
  return(self.fibonacci(K-1)+self.fibonacci(K-2))