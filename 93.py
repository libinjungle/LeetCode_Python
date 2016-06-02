class Solution(object):
  def restoreIpAddresses(self, s):
    """
    Three loop to parse string into four parts. Create a list hold these four parts
    and then check if this list is valid IP.
    Time, O(n3)
    Space, O(n3), inside each of three for loop, created a helper array

    :type s: str
    :rtype: List[str]
    """

    def is_valid(list):
      for s in list:
        # start with 0 but numerical value is not 0
        if s[0] == '0' and s != '0':
          return False
        if int(s) > 255:
          return False

      return True

    s_len = len(s)
    res = []
    for i in [1, 2, 3]:
      for j in [i+1, i+2, i+3]:
        for k in [j+1, j+2, j+3]:
          # test if k is out of range, k is the largest among i,j,k
          if (k >= s_len):
            continue

          s1 = s[:i]
          s2 = s[i:j]
          s3 = s[j:k]
          s4 = s[k:]
          if is_valid([s1, s2, s3, s4]):
            res.append('.'.join([s1, s2, s3, s4]))

    return res

if __name__ == '__main__':
  sol = Solution()
  res = sol.restoreIpAddresses("25525511135")
  print res




