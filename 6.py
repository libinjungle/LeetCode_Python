class solution(object):
  def zigzag(self, s, numRows):
    strarr = []

    for i in range(numRows):
      strarr.append("")

    idx = 0
    while (idx < len(s)):
      j = 0
      while (j < numRows and idx < len(s)):
        strarr[j] += s[idx]
        j += 1
        idx += 1

      k = numRows - 2

      while (k >= 1 and idx < len(s)):
        strarr[k] += s[idx]
        k -= 1
        idx += 1

    n = 1
    while (n < numRows):
      strarr[0] += strarr[n]
      n += 1

    return strarr[0]

  def zigzag2(self, s, numRows):
    '''
    :param s:
    :param numRows:
    :return:
    '''
    # create empty string list based on numRows

    strList = [''] * numRows
    idx, step = 0, 1

    # string is iterable
    for c in s:
      strList[idx] += c
      # in order
      if idx == 0:
        step = 1
      # reverse order
      elif idx == numRows - 1:
        step = -1

      idx += step
    # Combine lists into one list.
    return ''.join(strList)



if __name__ == '__main__':
  sol = solution()
  str = "PAYPALISHIRING"

  print sol.zigzag2(str, 3)

