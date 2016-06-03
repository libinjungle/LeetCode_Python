class Solution(object):
  def isOneEditDistance(self, s, t):
    """

    :type s: str
    :type t: str
    :rtype: bool
    """
    count = 0
    slen, tlen = len(s), len(t)
    if abs(slen-tlen) > 1 or s == t:
      return False
    if slen == tlen:
      for i in range(slen):
        if s[i] != t[i]:
          count += 1
          if count > 1:
            return False
      return True

    else:
      i, j = 0, 0
      if slen < tlen:
        while i < slen and j < tlen:
          if s[i] != t[j]:
            count += 1
            if count > 1:
              return False
            j += 1
          else:
            i += 1
            j += 1

      else:
        while i < tlen and j < slen:
          if t[i] != s[j]:
            count += 1
            if count > 1:
              return False
            j += 1
          else:
            i += 1
            j += 1

      return True

  def isOneEditDistance2(self, s, t):
    """
    make sure len(s) <= len(t). This simplifies the problem and
    helps reducing number of code lines
    corner case: s == t or the length difference is bigger than 1
    parse two strings at the same time. if char not equal, check un-parsed
    substrings to see if they are equal.
    Time: O(n)
    Space: 1

    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) > len(t):
      return self.isOneEditDistance(t, s)
    if abs(len(s) - len(t)) > 1 or s == t:
      return False
    for i in xrange(len(s)):
      if s[i] != t[i]:
        return s[i+1:] == t[i+1:] or s[i:] == t[i+1:]

if __name__ == '__main__':
  sol = Solution()
  s = ''
  t = ''
  print sol.isOneEditDistance2(s, t)

