def reverse(self, input):

  vowels = 'aeiou'
    
  start = 0
  end = len(input)-1
    
  l = list(input)
  # Can't use string because stings are immutable

  while start <= end:
    if input[start] not in vowels:
      start = start + 1
    elif input[end] not in vowels:
      end = end - 1
    else:
      l[start], l[end] = l[end], l[start]
      start = start + 1
      end = end - 1
  return "".join(l)