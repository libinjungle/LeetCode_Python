class Solution(object):
  def findStrobogrammatic(self, n):
    """
    top-down approach. f(n) = expand(f(n-2))
    :type n: int
    :rtype: List[str]
    """
    if n == 1:
      return ['0','1','8']
    if n == 2:
      return ['00', '11', '69', '88', '96']
    # depth first
    res = self.expand_once(self.findStrobogrammatic(n-2))
    return [s for s in res if s[0] != '0']

  def expand_once(self, list):
    newlist = []
    for s in list:
      newlist.append('1'+s+'1')
      newlist.append('0'+s+'0')
      newlist.append('8'+s+'8')
      newlist.append('6'+s+'9')
      newlist.append('9'+s+'6')
    return newlist

if __name__ == "__main__":
  sol = Solution()
  n = 6
  print sol.findStrobogrammatic(n)





