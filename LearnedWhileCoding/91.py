class Solution(object):
  '''
  Decode Ways.
  Given an encoded message containing digits,
  determine the total number of ways to decode it.
  '''
  def numDecodings(self, s):
    """
    dp solution
    corner case: 000001
    In order to handle this corner case which does not have encoding,
    we traverse from right to left. f(n) = f(n+1) + f(n+2).
    if it is 0, skip it. If s[i:i+2] bigger than 26, decoding[i] = decoding[i+1]
    Time, O(n), traverse digits string backward only once.
    Space, O(n) for dp array.

    :type s: str
    :rtype: int
    """

    if len(s) == 0:
      return 0
    # build dp array
    n = len(s)
    # CREATE A LIST WITH N+1 LENGTH AND INITIALIZE ALL ELEMENTS TO BE 0
    # decoding = [0] * (n+1)
    decoding = [0 for x in range(n+1)]
    decoding[n] = 1
    if s[n-1] == '0':
      decoding[n-1] = 0
    else:
      decoding[n-1] = 1

    # REVERSE INDEX
    for i in reversed(range(n-1)):
      if s[i] == '0':
        continue
      if int(s[i:i+2]) <= 26:
        decoding[i] = decoding[i+1] + decoding[i+2]
      else:
        decoding[i] = decoding[i+1]

    return decoding[0]


if __name__ == '__main__':
  sol = Solution()
  s = '100'
  print sol.numDecodings(s)






