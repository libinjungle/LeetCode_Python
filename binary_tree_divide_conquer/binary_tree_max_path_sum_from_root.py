class TreeNode(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class Solution(object):
  def maxPathSumFromRoot(self, root):
    """
    Divide_And_Conquer
    max sum is equal to the max of left and right child plus the root value.
    :param root:
    :return:
    """
    if root is None:
      return 0
    maxleft = self.maxPathSumFromRoot(root.left)
    maxright = self.maxPathSumFromRoot(root.right)
    return max(maxleft, maxright) + root.val

if __name__ == "__main__":
  sol = Solution()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)
  print(sol.maxPathSumFromRoot(root))

