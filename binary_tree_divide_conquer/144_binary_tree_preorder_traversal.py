# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def preorderTraversal(self, root):
    """
    divide and conquer
    :type root: TreeNode
    :rtype: List[int]
    """
    result = []
    if root == None:
      return result
    left = self.preorderTraversal(root.left)
    right = self.preorderTraversal(root.right)
    result.append(root.val)
    result += left
    result += right
    return result

if  __name__ == "__main__":
  sol = Solution()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)
  print sol.preorderTraversal(root)




