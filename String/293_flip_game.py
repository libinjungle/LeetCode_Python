class Solution(object):
  def generatePossibleNextMoves(self, s):
    """
    two pointers. move one step forward each time and check if there is two
    consecutive "+".
    time: O(n), parse string once
    space: no extra space except add string to result list

    :type s: str
    :rtype: List[str]
    """
    if len(s) < 2:
      return []

    res = []
    i = 0
    while i < len(s)-1:
      if s[i] == s[i+1] == '+':
        if i+2 < len(s):
          fliped = s[:i] + '--' + s[i+2:]
        else:
          fliped = s[:i] + '--'
        res.append(fliped)

      i += 1

    return res

if __name__ == '__main__':
  sol = Solution()
  s = "++++--+++--++++---++++++"
  print sol.generatePossibleNextMoves(s)





