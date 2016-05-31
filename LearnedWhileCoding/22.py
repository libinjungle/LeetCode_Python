class solution(object):
  def generateParenthesis(self, n):
    '''
    two recursions to update parenthesis got so far.
    :param n:
    :return:
    '''
    def tracking(res, s, open, close, n):
      if len(s) == 2 * n:
        res.append(s)
        return

      if (open < n):
        tracking(res, s+'(', open+1, close, n)
      if (close < open):
        tracking(res, s+')', open, close+1, n)


    res = []
    tracking(res, '', 0, 0, n)
    return res

if __name__ == '__main__':
  sol = solution()
  n = 4
  res = sol.generateParenthesis(n)
  print res

