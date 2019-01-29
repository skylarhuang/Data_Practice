class Solution(object):
  def reverseWords(self, input):
    """
    input: string input
    return: String
    """
    # write your solution here
    
    ls = input.split(' ')
    new_ls = []
    for wd in ls:
      if wd != '':
        new_ls.append(wd)
    new_ls = ' '.join(new_ls[::-1])
    new_ls = new_ls.strip()
    
    if len(new_ls) == 0:
      return ('')
    else:
      return new_ls