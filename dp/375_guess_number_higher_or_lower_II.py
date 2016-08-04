import sys

class Solution(object):
  def getMoneyAmount(self, n):
    """
    for each left to right, bottom to up

    start< k< end
    dp[j-1, j] is j-1 because in the worst case, j is picked, so the pay is j-1.
    dp[k] = k + max(dp[start, k-1], dp[k+1, end])
    only considering upper right matrix(i<j).
    in order to get dp[1][4], dp[1][1] and dp[3][4] must be already calculated.
    so i should be in decreasing order.

    :type n: int
    :rtype: int
    """
    # bottom-up approach
    dp = [[0]*(n+1) for _ in range(n+1)]
    for j in range(2, n+1):
      # 0 is not included.
      for i in range(j-1, 0, -1):
        globalmin = sys.maxint
        for k in range(i+1, j):
          # choose k but does not work. This is the maximum
          localmax = k + max(dp[i][k-1],  dp[k+1][j])
          # minimize the global cost, 二分法可能取得最小值
          globalmin = min(localmax, globalmin)
        if i+1 == j:
          dp[i][j] = i
        else:
          dp[i][j] = globalmin
    return dp[1][n]


  def getMoneyAmount2(self, n):
    """
    for each bottom to up, left to right.
    :param n:
    :return:
    """
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n, 0, -1):
      for j in range(i+1, n+1):
        # min(generator)
        dp[i][j] = min(x + max(dp[i][x-1], dp[x+1][j])
                       for x in range(i, j))
    return dp[1][n]









