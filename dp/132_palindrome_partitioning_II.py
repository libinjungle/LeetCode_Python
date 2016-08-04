class Solution(object):
  def minCut(self, s):
    """
    dp[i] is the min cut of previous i number of chars.
    initialize dp[len(s)] with each element to be its index minus 1.
    dp[i] = min(dp[j]+1, dp[i]) for j < i and j~i-1 is palindrome.
    time: O(n3)
    :type s: str
    :rtype: int
    """

    if not len(s):
      return 0
    # initialize dp[len(s)] with each element to be its index minus 1
    length = len(s)
    ispali = self.all_range_palindrome(s)
    dp = [i-1 for i in range(length+1)]
    for i in range(1, length+1):
      for j in range(0, i):
        if ispali[j][i-1]:
          # keep updating the minimum
          dp[i] = min(dp[j]+1, dp[i])
    return dp[length]

    # test if it is palindrome
  def ispanlindrome(self, s, i, j):
    while i < j:
      if s[i] != s[j]:
        return False
      i += 1
      j -= 1
    return True

    # check if palindrome for all range of substring

  def all_range_palindrome(self, s):
    length = len(s)
    palind_matrix = [[False]*length for _ in range(length)]

    for i in range(length):
      palind_matrix[i][i] = True
    for i in range(length-1):
      palind_matrix[i][i+1] = (s[i] == s[i+1])

    for j in range(2, length):
      for i in range(0, length-j):
        # small range is already calculated.
        palind_matrix[i][i+j] = self.ispanlindrome(s, i+1, i+j-1) and s[i] == s[i+j]
    return palind_matrix


if __name__ == "__main__":
  sol = Solution()
  s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  print(sol.minCut(s))







