class Solution(object):
  def numWays(self, n, k):
    """
    current one either paint the same color as previous one, or different.
    :type n: int
    :type k: int
    :rtype: int
    """

    if n == 0:
      return 0
    if n == 1:
      return k
    same, diff = k, k*(k-1)
    for i in range(3, n):
      same, diff = diff, diff*k
    return same + diff
