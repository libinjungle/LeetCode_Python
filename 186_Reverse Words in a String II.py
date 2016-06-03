class Solution(object):
  """
  parse word backward.
  :type s: a list of 1 length strings (List[str])
  :rtype: nothing
  """
  def reverseWords(self, s):
  # Used extra memory because of string concatation
  # Given an input string, reverse the string word by word.
  #  A word is defined as a sequence of non-space characters.
  #  The input string does not contain leading or trailing spaces
  # and the words are always separated by a single space.

    res = ''
    i = len(s) - 1
    end = len(s)
    while i >= 0:
      while s[i] != ' ' and i >= 0:
        i -= 1
      if i < 0:
        # Used extra memory because of string concanation
        res = res + s[i+1:end]
      else:
        res = res + s[i+1:end] + ' '
        end = i
        i = i - 1
    return res

  def reverseWords2(self, s):
    # in-place reverse
    s.reverse()
    start = 0
    for i in range(len(s)):
      if s[i] == ' ':
        # reversed is in-place reverse
        s[start:i] = reversed(s[start:i])
        start = i + 1

    s[start:] = reversed(s[start:])

if __name__ == '__main__':
  sol = Solution()
  s = list(['ab cd ed'])
  sol.reverseWords2(s)
  print s



