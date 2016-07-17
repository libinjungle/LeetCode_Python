class Solution(object):
  def countNumbersWithUniqueDigits(self, n):
    """
    dp.
    the number of unique digits on next level depends on this level.
    use a variable to record the previous level for the number of unique digits.
    :type n: int
    :rtype: int
    """
    if not n:
      return 1
    if n == 1:
      return 10

    count, prev = 10, 9
    i = 2
    while i <= n:
      count += (10-i+1)*prev
      prev = prev*(10-i+1)
      i += 1
    return count

if __name__ == "__main__":
  obj = Solution()
  print(obj.countNumbersWithUniqueDigits(6))





