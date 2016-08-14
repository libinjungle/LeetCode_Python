class Solution(object):
  def maxKilledEnemies(self, grid):
    """
    Traverse grid and record row_enemy_num and col_enemy_num before hit to wall,
    Because some cell don't need to recalculate row_enemy_num and col_enemy_num, this is
    memorization in DP. only reset row_enemy_num and col_enemy_num when row_index, col_index == 0 or (grid[i-1][j]
    or grid[i][j-1] is wall.

    :type grid: List[List[str]]
    :rtype: int
    """
    m = len(grid)
    n = len(grid[0]) if m > 0 else 0
    result = 0
    rowe = 0
    col = [0]*n
    # for in Python is really "foreach" that iterate over some iterable objects.
    for i in range(0, m):
      for j in range(0, n):
        # update col
        if not i or grid[i-1][j] == 'W':
          col[j] = 0
          for k in range(i, m):
            if grid[k][j] != 'W':
              col[j] += grid[k][j] == 'E'
            else:
              break
        # update row
        if not j or grid[i][j-1] == 'W':
          rowe = 0
          for k in range(j, n):
            if grid[i][k] != 'W':
              rowe += grid[i][k] == 'E'
            else:
              break

        if grid[i][j] == '0':
          result = max(result, rowe + col[j])
    return result


  def maxKilledEnemies2(self, grid):
    if not grid:
      return 0
    m = len(grid)
    n = len(grid[0])
    rowe = 0
    result = 0
    col = [0]*n
    for i, row in enumerate(grid):
      for j, cell in enumerate(row):
        if not i or grid[i-1][j] == 'W':
          col[j] = 0
          k = i
          while k < m and grid[k][j] != 'W':
            col[j] += grid[k][j] == "E"
            k += 1

        if not j or row[j-1] == 'W':
          rowe = 0
          k = j
          while k < n and grid[i][k] != "W":
            rowe += grid[i][k] == 'E'
            k += 1

        if cell == '0':
          result = max(result, rowe + col[j])
    return result


if __name__ == "__main__":
  sol = Solution()
  grid = [["0", "E", "E", "0"], ["W", "E", "0", "0"], ["0", "E", "E", "E"]]
  print(sol.maxKilledEnemies(grid))
