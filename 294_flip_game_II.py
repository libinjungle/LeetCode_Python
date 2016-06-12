class Solution(object):
  # My solution is not scalable. It can not handle complex cases
  # like "++++++++++++++++++++++++++"
  def canWin(self, s):
    helpposs = []
    helpposs.append([s])
    poss = []
    count = 0

    while count == 0 or len(helpposs) != 0:
      count += 1
      poss = list(helpposs)
      helpposs[:] = []
      for i in xrange(len(poss)):
        for j in xrange(len(poss[i])):
          run = self.flipgame(poss[i][j])
          if len(run) != 0:
            helpposs.append(run)
          else:
            if count%2 == 0:
              print "Guarantee!"
              return True

            else:
              print "Not guarantee"
              return False


  def flipgame(self, s):
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

  # def canWin2(self, s):
  #   if s == None or len(s) < 2:
  #     return False
  #   for i in xrange(len(s)-1):
  #     if

if __name__ == '__main__':
  sol = Solution()
  s = "+++++++++++++++++"
  print sol.canWin(s)
