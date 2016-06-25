class Solution(object):
  def isUgly(self, num):
    """
    base case: num < 1 and num == 1
    Recursively check if num can be divided by 2, 3 and 5. If not, it is
    not ugly number. If num can be divided by one of them, update num.
    
    :type num: int
    :rtype: bool
    """
    if num < 1:
      return False
    if num == 1:
      return True
    if num%3 != 0 and num%2 != 0 and num%5 != 0:
      return False
    if num%2 == 0:
      num = num/2
      return self.isUgly(num)
    elif num%3 == 0:
      num = num/3
      return self.isUgly(num)
    elif num%5 == 0:
      num = num/5
      return self.isUgly(num)

if __name__ == "__main__":
  solu = Solution()
  num = 127
  print solu.isUgly(num)