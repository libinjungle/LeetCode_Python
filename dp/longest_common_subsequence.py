class Solution(object):
  def longest_common_subsequence(self, s1, s2):
    """
    use matrix to solve two sequence dp problem

    function
    --------
    dp[i][j] represents LCS of previous i chars of s1 and previous j chars of s2

    state
    -----
    if s1[i] == s2[j], dp[i][j] = dp[i-1][j-1]+1
    if s1[i] != s2[j], dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    initial
    -------
    since LCS of empty string and previous i is 0,
    dp[i][0] = 0
    dp[0][j] = 0

    time: O(n2)
    :param s1: string
    :param s2: string
    :return:
    """
    m = len(s1)
    n = len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
      for j in range(1, n+1):
        if s1[i-1] == s2[j-1]:
          dp[i][j] = dp[i-1][j-1] + 1
        else:
          dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]


if __name__ == "__main__":
  sol = Solution()
  s1 = "hello"
  s2 = "heroin"
  print(sol.longest_common_subsequence(s1,s2))
