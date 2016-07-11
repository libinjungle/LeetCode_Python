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

  def postorderTraversal1(self, root):
    """
    not sure if I can use recursion inside iteration during interview.
    :param root:
    :return:
    """
    result = []
    if root is None:
      return result
    stack = []
    while len(stack) != 0 or root is not None:
      if root is None:
        node = stack.pop()
        subresult = self.postorderTraversal1(node.right)
        result += subresult
        result.append(node.val)
      else:
        stack.append(root)
        root = root.left
    return result

  def postorderTraversal2(self, root):
    """
    reverse of preorder of root, right, left
    :param root:
    :return:
    """
    res, stack = [], [root]
    while stack:
      tmp = stack.pop()
      if tmp:
        res.append(tmp.val)
        stack.append(tmp.left)
        stack.append(tmp.right)
    return res[::-1]

if __name__ == "__main__":
  sol = Solution()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)
  print sol.postorderTraversal1(root)

