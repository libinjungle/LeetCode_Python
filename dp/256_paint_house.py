class Solution(object):
  def minCost(self, costs):
    """
    each position has three variables.
    1. minimum cost if paint current cell as red
    2. minimum cost if paint current cell as blue
    3. minimum cost if paint current cell as green

    :type costs: List[List[int]]
    :rtype: int
    """
    lastred = costs[0][0]
    lastblue = costs[0][1]
    lastgreen = costs[0][2]
    for i in range(1, len(costs)):
      curred = costs[i][0] + min(lastblue, lastgreen)
      curblue = costs[i][1] + min(lastred, lastgreen)
      curgreen = costs[i][2] + min(lastred, lastblue)

      lastred = curred
      lastblue = curblue
      lastgreen = curgreen
    return min(lastred, lastblue, lastgreen)


if __name__ == "__main__":
  sol = Solution()



