class Solution(object):
  def calculate(self, s):
    """
    Stack implementation of Calculator
    Assume the equation is valid. initial sign is "+". if sign is + or -,
    push previous number with sign. If "*" or "/", pop the stack and do multiplition
    or division with the number.
    Time: O(N)
    Space: O(N) for push characters on stack
    :type s: str
    :rtype: int
    """
    if not s:
      return '0'
    opers = ['+', '-', '*', '/']
    stack, sign, num = [], '+', 0
    # NOTICE THIS FOR LOOP, IT IS DELAY FOR LOOP
    for i in xrange(len(s)):
      # CHECK IF CHAR IS DIGIT.
      if s[i].isdigit():
        num = num*10+int(s[i])
      # handler end of equation
      if s[i] in opers or i == len(s) - 1:
        # put a default + sign
        # +3-2*5
        if sign == '+':
          stack.append(num)
        elif sign == '-':
          stack.append(-num)
        elif sign == '*':
          stack.append(stack.pop()*num)
        elif sign == '/':
          # int(-1.5) = -1
          stack.append(int(stack.pop()/float(num)))

        sign = s[i]
        # for next number
        num = 0

    res = sum(stack)

    return res

if __name__ == '__main__':
  sol = Solution()
  s = ""
  res = sol.calculate(s)
  #print int(-3/float(2))
  print res

### OUTPUT ###
# 0
