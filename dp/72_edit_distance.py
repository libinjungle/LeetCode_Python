class Solution(object):
  def minDistance(self, word1, word2):
    """
    initial
    -------
    empty string to f[i] needs ith edit.
    f[i][0] = i
    f[0][j] = j

    :type word1: str
    :type word2: str
    :rtype: int
    """

    m = len(word1)
    n = len(word2)
    # creat matrix
    f = [[0]*(n+1) for _ in range(m+1)]
    # initialization
    for i in range(0, m+1):
      f[i][0] = i
    for j in range(0, n+1):
      f[0][j] = j
    # state
    for i in range(1, m+1):
      for j in range(1, n+1):
        # f[i][j] represents previous i and j, so word index should be i-1 and j-1
        if word1[i-1] == word2[j-1]:
          f[i][j] = min(f[i-1][j-1], f[i-1][j]+1, f[i][j-1]+1)
        else:
          f[i][j] = min(f[i-1][j-1], f[i-1][j], f[i][j-1]) + 1
    return f[m][n]


if __name__ == "__main__":
  sol = Solution()
  s1 = "hello"
  s2 = "heroin"
  print(sol.minDistance(s1,s2))


