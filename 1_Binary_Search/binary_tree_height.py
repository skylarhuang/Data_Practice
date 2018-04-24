def findHeight(self, root):
    """
    input: TreeNode root
    return: int
    """
  # write your solution here
  if not root:
    return 0

  left = self.findHeight(root.left)
  right = self.findHeight(root.right)
     
  return max(left,right)+1

