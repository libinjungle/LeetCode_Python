import math

class Solution(object):
  def maximalSquare(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """

    m = len(matrix)
    n = len(matrix[0])
    maxsquare = 0
    for j in range(0, n):
      if matrix[0][j] == 1:
        maxsquare = 1
        break
    if maxsquare == 0:
      for i in range(0, m):
        if matrix[i][0] == 1:
          maxsquare = 1
          break

    for i in range(1, m):
      for j in range(1, n):
        if matrix[i][j] == 0 or \
          matrix[i-1][j] == 0 or \
          matrix[i-1][j-1] == 0 or \
          matrix[i][j-1] == 0:
          continue
        if matrix[i-1][j] == matrix[i][j-1] == matrix[i-1][j-1]:
          matrix[i][j] = math.pow(math.sqrt(matrix[i-1][j]) + 1, 2)
        else:
          matrix[i][j] = math.pow(math.sqrt(min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1])) + 1, 2)
        if maxsquare < matrix[i][j]:
            maxsquare = matrix[i][j]
    return int(maxsquare)


if __name__ == "__main__":
  sol = Solution()
  matrix = [[1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]]
  print(sol.maximalSquare(matrix))



