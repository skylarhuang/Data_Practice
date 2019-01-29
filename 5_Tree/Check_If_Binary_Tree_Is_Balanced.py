class Solution(object):
  def isBalanced(self, root):
    """
    input: TreeNode root
    return: boolean
    """
    # write your solution here
    if not root:
      return True
    
    left_, right_ = self.getHeight(root.left), self.getHeight(root.right)
    left, right = self.isBalanced(root.left), self.isBalanced(root.right)
    
    return left and right and abs(left_ - right_)<=1

    
  def getHeight(self, root):
    if not root: return 0
    
    left, right = self.getHeight(root.left), self.getHeight(root.right)
    return max(left, right)+1