def shortestDistance(self, words, word1, word2): 
  i1 = None
  i2 = None
  d = len(words)+1
    
  for i in range(len(words)):
    if words[i] == word1:
      i1 = i
    elif words[i] == word2:
      i2 = i
      
    if i1 is not None and i2 is not None:
      d = min(d, abs(i1-i2))
        
  return(d)