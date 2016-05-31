
class solution(object):
  '''
  Multiply Strings.
  The calculation is backward naturally. To make it easy to tack the update of
  each position, reverse string and do the multiplication forward.
  Note: python does not support '1' - '0'
  '''
  def multiply(self, num1, num2):
    # holding all integers in a format of list
    res = [0] * (len(num1)+len(num2))
    # reverse string and do the multiplication
    # enumerate returns a list of tuple with index and element as members
    for i, e1 in enumerate(reversed(num1)):
      for j, e2 in enumerate(reversed(num2)):
        res[i+j] += int(e1)*int(e2)
        res[i+j+1] = res[i+j]/10
        res[i+j] = res[i+j] % 10
    # get rid of extra 0. if the product is 0, leave it there.
    while len(res) > 1 and res[-1] == 0:
      res.pop()
    # reverse back
    return ''.join(map(str, res[::-1]))

if __name__ == '__main__':
  sol = solution()
  res = sol.multiply('1211', '11')
  print res

