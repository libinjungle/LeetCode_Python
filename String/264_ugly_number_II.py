class Solution(object):
  def nthUglyNumber(self, n):
    """
    each ugly number is 2, 3, or 5 multiply by a smaller ugly number.
    how to solve the order problem? make sure each time the smallest number
    is added to the final result list.
    Your solution is excellent! This is actually three pointers solution.
    After multiplications, update the pointer that has the smallest value.
    :type n: int
    :rtype: intclass Solution(object):
  def nthUglyNumber(self, n):
    """
    each ugly number is 2, 3, or 5 multiply by a smaller ugly number.
    how to solve the order problem? make sure each time the smallest number
    is added to the final result list.
    Your solution is excellent! This is actually three pointers solution.
    After multiplications, update the pointer that has the smallest value.
    :type n: int
    :rtype: int
    """
    ugly = [1]
    i2, i3, i5 = 0, 0, 0
    while n > 1:
      u2, u3, u5 = 2*ugly[i2], 3*ugly[i3], 5*ugly[i5]
      umin = min(u2, u3, u5)
      ugly.append(umin)
      # Note that u2, u3, u5 may have the same value. To avoid duplication,
      # update all indexes.
      if umin == u2:
        i2 += 1
      if umin == u3:
        i3 += 1
      if umin == u5:
        i5 += 1

      n -= 1
    return ugly[-1]


if __name__ == '__main__':
  sol = Solution()
  n = 20
  print sol.nthUglyNumber(n)
    """
    ugly = [1]
    i2, i3, i5 = 0, 0, 0
    while n > 1:
      u2, u3, u5 = 2*ugly[i2], 3*ugly[i3], 5*ugly[i5]
      umin = min(u2, u3, u5)
      ugly.append(umin)
      # Note that u2, u3, u5 may have the same value. To avoid duplication,
      # update all indexes.
      if umin == u2:
        i2 += 1
      if umin == u3:
        i3 += 1
      if umin == u5:
        i5 += 1

      n -= 1
    return ugly[-1]


if __name__ == '__main__':
  sol = Solution()
  n = 20
  print sol.nthUglyNumber(n)