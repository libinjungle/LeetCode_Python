class Solution(object):
  def isInterleave(self, s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    x = len(s1)
    y = len(s2)
    z = len(s3)
    if x+y != z:
      return False
    if not s1:
      return s2 == s3
    if not s2:
      return s1 == s3
    f = [[False]*(y+1) for _ in range(x+1)]
    f[0][0] = True

    for i in range(1, x+1):
      if s1[:i] == s3[:i]:
        f[i][0] = True
    for j in range(1, y+1):
      if s2[:j] == s3[:j]:
        f[0][j] = True
    print(f)
    for i in range(1, x+1):
      for j in range(1, y+1):
        f[i][j] = (f[i-1][j] and (s1[i-1] == s3[i+j-1])) or \
                  (f[i][j-1] and (s2[j-1] == s3[i+j-1]))

    return f[x][y]


if __name__ == "__main__":
  sol = Solution()
  s1 = "db"
  s2 = "b"
  s3 = "cbb"
  print(sol.isInterleave(s1, s2, s3))



