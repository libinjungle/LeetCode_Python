class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = self.helper(1, num, num)
        if x*x == num:
            return True
        return False
    def helper(self, a, b, num):
      if a >= b:
        return b
      mid = a + (b-a)/2
      if mid*mid == num:
        return mid
      elif mid*mid < num:
        a = mid + 1
        return self.helper(a, b, num)
      else:
        b = mid-1
        return self.helper(a, b, num)

if __name__ == "__main__":
  sol = Solution()
  print(sol.isPerfectSquare(25))
