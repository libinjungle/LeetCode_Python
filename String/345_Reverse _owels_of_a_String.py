import re

class Solution(object):
  def reverseVowels(self, s):
    '''
    two-pointers traversing. One from the beginning and the other from
    the end. Stop at vowels and reverse these two vowels.
    :param s:
    :return:
    time: O(n), parse the string only once
    space: O(n), use an extra list to store characters and then convert to string
    '''
    # base case
    if s == '' or len(s) == 1:
      return s

    vowels = "aoeiuAOEIU"
    start, end = 0, len(s)-1
    res = [""]*len(s)
    while start < end:
      while start<end and s[start] not in vowels:
        res[start] = s[start]
        start += 1
      while start<end and s[end] not in vowels:
        res[end] = s[end]
        end -= 1

      res[start] = s[end]
      res[end] = s[start]
      start += 1
      end -= 1
    # if start meets end, this character needs to be added to result.
    if start == end:
      res[start] = s[start]
    # use join to convert list to string
    return "".join(res)

  def reverse_vowels2(self, s):
    '''
    use regular expression to reverse vowels.
    :param s:
    :return:
    '''
    # reverse all vowels
    vowels = (c for c in reversed(s) if c in "aoeiuAOEIU")
    print vowels
    # re.sub(pattern, repl, string)
    # (?i) is case insensitive match. next() is like iterator which retrieve
    # the next element.
    return re.sub('(?i)[aoeiu]', lambda x : next(vowels), s)

if __name__ == "__main__":
  sol = Solution()
  s = 'leetcode'
  print sol.reverse_vowels2(s)




