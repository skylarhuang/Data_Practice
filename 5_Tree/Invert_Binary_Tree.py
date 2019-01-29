# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def invertTree(self, root):
    """
    input: TreeNode root
    return: TreeNode
    """
    # write your solution here
    res = root
    if not root:
      return root
    else:
      root.left, root.right = root.right, root.left
      
    self.invertTree(root.left)
    self.invertTree(root.right)
    
    return res