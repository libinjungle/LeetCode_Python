class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = list(s)
        start, end = 0, len(s)-1
        while start < end:
          tmp = slist[start]
          slist[start] = slist[end]
          slist[end] = tmp
          start += 1
          end -= 1
        return ''.join(slist)

    def reverseString2(self, s):
      return s[::-1]

if __name__ == "__main__":
  sol = Solution()
  s = ' asda1b'
  print sol.reverseString2(s)