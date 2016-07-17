from collections import deque
import sys

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution(object):

  """
  These are class or static variables. Use self.prev and self.firstnode to
  access them inside a function.

  """

  prev = -sys.maxint-1
  firstnode = True

  def isValidBST(self, root):
    """
    similar to inorder traverse. If this is an valide BST, the inorder traverse
    should be in order.
    record previous poped up node. Then compare with the
    current poped up node.
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
      return False
    stack = deque()
    prev = None
    while root or stack:
      if root:
        stack.append(root)
        root = root.left
      else:
        node = stack.pop()
        if prev and prev.val > node.val:
          return False
        prev = node
        root = node.right
    return True



  def isValidBST2(self, root):
    """
    recursive solution.
    :param root:
    :return:
    """

    if not root:
      return True
    if not self.isValidBST2(root.left):
      return False
    if not self.firstnode and self.prev >= root.val:
      return False

    self.firstnode = False
    self.prev = root.val
    if not self.isValidBST2(root.right):
      return False
    return True


if __name__ == "__main__":
  sol = Solution()
  root = TreeNode(3)
  root.left = TreeNode(1)
  root.right = TreeNode(4)
  root.left.left = TreeNode(0)
  root.left.right = TreeNode(2)
  print(sol.isValidBST2(root))









