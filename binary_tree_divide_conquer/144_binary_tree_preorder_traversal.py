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

  def preorderTraversal1(self, root):
    """
    Iterative solution
    preorder: add root, left child and right child in order
    add node's value to result and node to stack while traverse the tree. exhaust left child in DFS way.
    if left child is null, pop node out of stack and exhaust right children.
    Time: O(n)
    Space: O(n)
    :param root:
    :return:
    """
    result = []
    if root is None:
      return result
    stack = []
    # if not root block will execute if root is None.
    while len(stack) != 0 or root is not None:
      if root is None:
        root = stack.pop().right
      else:
        stack.append(root)
        result.append(root.val)
        root = root.left
    return result

if  __name__ == "__main__":
  sol = Solution()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)
  print sol.preorderTraversal1(root)




