class Solution(object):
  def isInterleaving(self, s1, s2, s3):
    x = len(s1)
    y = len(s2)
    z = len(s3)
    if x+y != z:
      return False
    dp = [[False]*(y+1) for _ in range(x+1)]
    dp[0][0] = True
    for i in range(1, x+1):
      dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
    for j in range(1, y+1):
      dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

    for i in range(1, x+1):
      for j in range(1, y+1):
          dp[i][j] = (dp[i-1][j] and s3[i+j-1] == s1[i-1]) or (dp[i][j-1] and s3[i+j-1] == s2[j-1])
    return dp[x][y]



