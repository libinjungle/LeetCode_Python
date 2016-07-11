import sys

class TreeNode(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class Solution(object):
  def max_path_sum(self, root):
    """
    singlepath: from node to any. Not necessary to have node. Minimum is 0.
    maxpath:    can be any path in tree. at least one node. Does not have minimum.
    max sum of any_to_any is max(maxpath_left, maxpath_right, singlepath_left+singlepath_right+root)
    :param root: TreeNode
    :return:
    """
    node = self.helper(root)
    return node.maxpath

  def helper(self, root):
    if root is None:
      return MyTreeNode(0, -sys.maxint-1)
    # divide
    left = self.helper(root.left)
    right = self.helper(root.right)
    singlepath = max(left.singlepath, right.singlepath) + root.val
    singlepath = max(0, singlepath)
    maxpath = max(left.maxpath, right.maxpath)
    maxpath = max(maxpath, left.singlepath+right.singlepath+root.val)
    return MyTreeNode(singlepath, maxpath)


class MyTreeNode(object):
  def __init__(self, singlepath, maxpath):
    self.singlepath = singlepath
    self.maxpath = maxpath

if __name__ == "__main__":
  sol = Solution()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)
  print(sol.max_path_sum(root))