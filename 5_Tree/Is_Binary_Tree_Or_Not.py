class Solution(object):
  def isBST(self, root):
    """
    input: TreeNode root
    return: boolean
    """
    # write your solution here    
    return self.helper(root, float('-inf'), float('inf'))

  def helper(self, root, lo, hi):
    if not root:
      return True
    if root.val <= lo or root.val >= hi:
      return False
    return self.helper(root.left, lo, root.val) and self.helper(root.right, root.val, hi)