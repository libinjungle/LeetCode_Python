import collections

class Solution(object):
  def isStrobogrammatic(self, num):
    """
    two pointers. If two chars are not symmetric, num is not strobogrammatic.
    notice that 6 is symmetric with 9.
    :type num: str
    :rtype: bool
    """
    deque = collections.deque(map(int, list(num)))
    while len(deque) >= 2:
      l, r = deque.popleft(), deque.pop()
      if not self.isSymmetric(l, r):
        return False
      l += 1
      r -= 1
    return not deque or deque.pop() in [0,1,8]

  def isSymmetric(self, n1, n2):
    set = {(6,9), (9,6), (1,1), (8,8), (0,0)}
    if (n1, n2) not in set:
      return False
    return True

if __name__ == '__main__':
  sol = Solution()
  num = '10001'
  print sol.isStrobogrammatic(num)
  print ord('a')


