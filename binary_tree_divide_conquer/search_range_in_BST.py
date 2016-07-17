# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  """
  given a range from k1 to k2. find all nodes in BST that in this range.
  solution: when to move to left subtree, root > k1; when to move to right subtree, root < k2
            when to add to result list, k1 <= root <= k2.
  """
  res = []

  def search_range_in_BST(self, root, k1, k2):
    self.helper_search_range_in_BST(root, k1, k2)
    return self.res

  # updating res, don't return anything.
  def helper_search_range_in_BST(self, root, k1, k2):
    if not root:
      return
    if root.val > k1:
      self.search_range_in_BST(root.left, k1, k2)
    if root.val >= k1 and root.val <= k2:
      self.res.append(root.val)
    if root.val < k2:
      self.search_range_in_BST(root.right, k1, k2)


if __name__ == "__main__":
  sol = Solution()
  root = TreeNode(3)
  root.left = TreeNode(1)
  root.right = TreeNode(4)
  root.left.left = TreeNode(0)
  root.left.right = TreeNode(2)
  print(sol.search_range_in_BST(root, 0, 4))




