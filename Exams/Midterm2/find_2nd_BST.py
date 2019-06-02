class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

head = TreeNode(3)
head.left = TreeNode(1)
head.right = TreeNode(5)
head.left.right = TreeNode(2)
head.left.left = TreeNode(0)
head.right.right = TreeNode(7)


def find_largest(root):
    if not root:
        return
    if not root.right:
        return root
    return find_largest(root.right)


def find_2nd_largest(root):

    if not root:
        return

    if not root.right:
        return find_largest(root.left)

    right_ = root.right
    if not right_.left and not right_.right:
        return root
    return find_2nd_largest(root.right)


x = find_2nd_largest(head)
print(x.val)


def find_smallest(root):
    if not root:
        return
    if not root.left:
        return root
    return find_smallest(root.left)

def find_2nd_smallest(root):
    if not root:
        return
    if not root.left:
        return find_smallest(root.right)

    left_ = root.left
    if not left_.left and not left_.right:
        return root
    return find_2nd_smallest(root.left)

x = find_2nd_smallest(head)
print(x.val)