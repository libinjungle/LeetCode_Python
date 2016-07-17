from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def levelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    res = []
    if not root:
      return []
    queue = deque()
    queue.append(root)
    while queue:
      size = len(queue)
      sublist = []
      while size > 0:
        node = queue.popleft()
        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)
        sublist.append(node.val)
        size -= 1
      res.append(sublist)
    return res

if __name__ == "__main__":
  sol = Solution()
  root = None
  # root = TreeNode(1)
  # root.left = TreeNode(2)
  # root.right = TreeNode(3)
  # root.left.left = TreeNode(4)
  # root.left.right = TreeNode(5)
  level_order_nodes = sol.levelOrder(root)
  print(level_order_nodes)







