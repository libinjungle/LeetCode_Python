class solution(object):
  '''
  Given a string S, find the longest palindromic substring in S
  '''
  maxLen = 0
  start = 0

  def longest_palindromic_substring(self, s):
    '''
    for each index, get the longest palindromic substring. Update the maxLen
    :return:
    '''
    # base case
    if len(s) < 2:
      return s
    for i in range(len(s)-1):
      self.sublongest(s, i, i)
      self.sublongest(s, i, i+1)

    return s[self.start:self.start+self.maxLen]

  def sublongest(self, s, i, j):
    '''
    i == j or i == (j - 1), for odd length palindrome and even length palindrome respectively.
    This function updates starting index and length of substring.
    '''
    while i >= 0 and j < len(s) and s[i] == s[j]:
      i -= 1
      j += 1

    Len = j-i-1
    if Len > self.maxLen:
      self.maxLen = Len
      self.start = i+1

if __name__ == '__main__':
  sol = solution()
  str = 'ababbbbbbabacdefggfedca'
  print sol.longest_palindromic_substring(str)
