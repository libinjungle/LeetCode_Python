
def generateParenthesis(n):
  def track(s, open, close, paren=[]):
    if open:          track(s+'(', open-1, close)
    if close > open:  track(s+')', open, close-1)
    # Why it must have a comma here???
    if not close:     paren += s,
    return paren

  return track('', n, n)

print generateParenthesis(3)



