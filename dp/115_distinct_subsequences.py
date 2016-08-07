class Solution(object):
  def numDistinct(self, s, t):
    """
    state
    -----
    f[i][j] represents how many distinct subsequences of previous j chars of t
    does previous i chars of s have

    function
    --------
    f[i][j] = f[i-1][j-1] + f[i-1][j] if s[i] == t[j]
    f[i][j] = f[i-1][j] if s[i] != t[j]

    initial
    -------
    f[0][j] = 0
    f[i][0] = 1

    :type s: str
    :type t: str
    :rtype: int
    """
    m = len(s)
    n = len(t)
    f = [[0]*(n+1) for _ in range(m+1)]
    # empty string is a subsequence of any string
    for j in range(0, n+1):
      f[0][j] = 0
    for i in range(0, m+1):
      f[i][0] = 1
    for i in range(1, m+1):
      for j in range(1, n+1):
        if s[i-1] == t[j-1]:
          f[i][j] = f[i-1][j-1] + f[i-1][j]
        else:
          f[i][j] = f[i-1][j]
    return f[m][n]


if __name__ == "__main__":
  sol = Solution()
  s = "rabbbbit"
  t = "rabit"
  print(sol.numDistinct(s,t))
