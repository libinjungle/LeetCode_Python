# Definition for a  binary tree node

from collections import deque

class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class BSTIterator(object):
  def __init__(self, root):
    """
    store in-order nodes up front. Not memory efficient.

    :type root: TreeNode
    """
    self.iter = deque()
    stack = deque()
    while root or stack:
      if root:
        stack.append(root)
        root = root.left
      else:
        node = stack.pop()
        self.iter.append(node.val)
        root = node.right

  def hasNext(self):
    """
    :rtype: bool
    """
    if len(self.iter) > 0:
      return True
    return False

  def next(self):
    """
    :rtype: int
    """
    if self.hasNext():
      return self.iter.popleft()
    return None

class BSTIterator2(object):
  def __init__(self, root):
    self.cur = root
    self.stack = deque()

  def hasNext(self):
    if self.cur or self.stack:
      return True
    return False

  def next(self):
    if self.hasNext():
      while self.cur:
        self.stack.append(self.cur)
        self.cur = self.cur.left
      node = self.stack.pop()
      self.cur = node.right
      yield node.val




if __name__ == "__main__":
  root = TreeNode(3)
  root.left = TreeNode(1)
  root.right = TreeNode(4)
  root.left.left = TreeNode(0)
  root.left.right = TreeNode(2)

  i, v = BSTIterator2(root), []
  while i.hasNext():
    v.append(i.next())
  print(v)

    # Your BSTIterator will be called like this:
    # i, v = BSTIterator(root), []
    # while i.hasNext(): v.append(i.next())