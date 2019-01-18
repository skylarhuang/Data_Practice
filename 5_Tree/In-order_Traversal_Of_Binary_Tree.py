# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def inOrder(self, root):
    """
    input: TreeNode root
    return: Integer[]
    """
    # write your solution here
    res = []
    self.help(root, res)
    return res
  
  def help(self, root, res):
    if not root:
      return
    else:
      self.help(root.left, res)
      res.append(root.val)
      self.help(root.right, res)
