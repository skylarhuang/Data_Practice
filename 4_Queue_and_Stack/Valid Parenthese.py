class Solution(object):
  def isValid(self, s):
    """
    input: string s
    return: boolean
    """
    # write your solution here
    l = []
    
    for si in range(len(s)):
      if s[si] in '([{':
        l.append(s[si])
      elif s[si] == ')':
        if l==None or l.pop()!='(':
          return False
      elif s[si] == ']':
        if l==None or l.pop()!='[':
          return False        
      elif s[si] == '}':
        if l==None or l.pop()!='{':
          return False        
    
    if len(l) != 0:
      return False
    else:
      return True