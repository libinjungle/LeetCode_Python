# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def postorderTraversal(self, root):
    """
    recursive. divide and conquer
    :type root: TreeNode
    :rtype: List[int]
    """
    result = []
    if root == None:
      return result
    left = self.postorderTraversal(root.left)
    right = self.postorderTraversal(root.right)
    result += left
    result += right
    result.append(root.val)
    return result

if __name__ == "__main__":
  sol = Solution()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)
  print sol.postorderTraversal(root)

