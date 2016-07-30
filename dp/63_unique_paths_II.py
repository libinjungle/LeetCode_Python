class Solution(object):
  def uniquePathsWithObstacles(self, obstacleGrid):
    """
    calculate path num for the first row. For the first row, if has obstracle,
    all cells after it are marked by 0. Then solve other rows.
    Time: O(n2)
    Space: O(1)
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    for i in range(n):
      if obstacleGrid[0][i] == 1:
        for j in range(i, n):
          obstacleGrid[0][j] = 0
        break
      else:
        obstacleGrid[0][i] = 1

    for i in range(1, m):
      for j in range(n):
        if obstacleGrid[i][j] == 1:
          obstacleGrid[i][j] = 0
        else:
          if j == 0:
            obstacleGrid[i][j] = obstacleGrid[i-1][j]
          else:
            obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
    return obstacleGrid[m-1][n-1]


  def uniquePathsWithObstacles2(self, obstacleGrid):
    """
    use extra grid.
    :param obstacleGrid:
    :return:
    """
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    paths = [[0 for _ in range(n)] for _ in range(m)]
    # first row
    for i in range(n):
      if obstacleGrid[0][i] != 1:
        paths[0][i] = 1
      else:
        break
    # first column
    for i in range(m):
      if obstacleGrid[i][0] != 1:
        paths[i][0] = 1
      else:
        break
    for i in range(1, m):
      for j in range(1, n):
        if obstacleGrid[i][j] != 1:
          paths[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
    return paths[m-1][n-1]



if __name__ == "__main__":
  sol = Solution()
  matrix = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
  ]
  print(sol.uniquePathsWithObstacles(matrix))

