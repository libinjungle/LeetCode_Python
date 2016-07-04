class Solution(object):
  def minWindow(self, s, t):
    if len(t) > len(s):
      return ""
    #mark occurrences of each char in t
    left, right = 0, 0
    count = len(t)
    min_len = len(s)
    min_str = ""
    occur = {}
    for c in t:
      if c in occur:
        occur[c] += 1
      else:
        occur[c] = 1
    # pass s
    for i in range(len(s)):
      if s[i] not in occur:
        continue
      if occur[s[i]] > 0:
        count -= 1
      occur[s[i]] -= 1
      if count == 0:
        while s[left] not in occur or occur[s[left]] < 0:
          if s[left] in occur:
            occur[s[left]] += 1
          left += 1
        if min_len > i-left+1:
          min_len = i-left+1
          min_str = s[left:i+1]
    if count != 0:
      return ""
    return min_str









if __name__ == "__main__":
  sol = Solution()
  S = "a"
  T = "b"
  print sol.minWindow(S, T)




