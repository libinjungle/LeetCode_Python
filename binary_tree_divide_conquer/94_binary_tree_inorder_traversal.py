# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def inorderTraversal(self, root):
    """
    recursive. divide and conquer
    :type root: TreeNode
    :rtype: List[int]
    """
    result = []
    if root == None:
      return result
    left = self.inorderTraversal(root.left)
    result += left
    result.append(root.val)
    right = self.inorderTraversal(root.right)
    result += right
    return result

  def inorderTraversal1(self, root):
    """
    inorder: add left children first, then parent and right children.
    exhaust left children first, then add the value of node that is poped out of stack.
    then pass right child of the poped node as root.
    Time: O(n)
    Space: O(n)
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
        result.append(node.val)
        root = node.right
      else:
        stack.append(root)
        root = root.left
    return result

if  __name__ == "__main__":
  sol = Solution()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)
  print sol.inorderTraversal1(root)
