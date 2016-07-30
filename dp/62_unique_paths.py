class Solution(object):
  def uniquePaths(self, m, n):
    """
    since robot can only move to right or down, it guarantees that it will
    reach the right bottom corner.
    f(i, j) = f(i-1, j) + f(i, j-1)

    :type m: int
    :type n: int
    :rtype: int
    """
    # using list comprehensions to intialize two dimentional array
    matrix = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
      matrix[i][0] = 1
    for j in range(n):
      matrix[0][j] = 1
    for i in range(1, m):
      for j in range(1, n):
        matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
    return matrix[m-1][n-1]

if __name__ == "__main__":
  sol = Solution()
  num_paths = sol.uniquePaths(5, 5)
  print(num_paths)




