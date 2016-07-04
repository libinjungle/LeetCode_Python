class Solution(object):
  def minWindow(self, s, t):
    """
    use dict to store char and their occurrences in t. use a count that is initialized to be the length of t. use
    a pointer called left to mark the left index of matched substring. go over s and reduce occurrence of char in t
    by one in dict and reduce count by one. when count is zero, we find matched substring. Then Keep moving index in s
    and updating the left index. When to update left index? if left char is not in t or left char's
    occurrence is less than 0.

    :type s: str
    :type t: str
    :rtype: str
    """

    if t == "" or s == "" or len(s) < len(t):
      return ""

    left, count = 0, len(t)
    matched, minlen = s, len(s)
    start, end = 0, len(s)-1
    tchars = {}
    # populate dict that has chars and their occurrences.
    for i in range(len(t)):
      if t[i] in tchars:
        tchars[t[i]] += 1
      else:
        tchars[t[i]] = 1

    for i in range(len(s)):
      if s[i] in tchars:
        if tchars[s[i]] > 0:
          count -= 1
        tchars[s[i]] -= 1
      if count == 0:
        # update left index
        while s[left] not in tchars or tchars[s[left]] < 0:
          if s[left] in tchars:
            tchars[s[left]] += 1
          left += 1
        if minlen > i-left+1:
          start = left
          end = i
          minlen = i-left+1

    if count != 0: return ""
    return s[start:end+1]

if __name__ == "__main__":
  sol = Solution()
  S = "a"
  T = "b"
  print sol.minWindow(S, T)




