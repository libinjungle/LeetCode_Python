class Solution(object):
  def wordBreak(self, s, wordDict):
    """
    state:
    ---------
    dp[i] represents whether previous i chars can be broke into words in dict.

    initialize:
    ---------
    dp[0] is true

    function:
    ---------
    dp[i] == true if dp[j] is true and j < i and s[j:i-1] is a word in dict.

    time: O(nl), l is max length of dict word.
    :type s: str
    :type wordDict: Set[str]
    :rtype: bool
    """
    if len(wordDict) == 0:
      return False
    length = len(s)
    # create list that has length+1 number of False
    dp = [False]*(length+1)
    dp[0] = True
    maxlen = self.maxlenword(wordDict)
    for i in range(1, length+1):
      # since j is in the range of maxlen, it's better to use i-j~i as the range
      for j in range(1, i+1) and range(1, maxlen+1):
        if not dp[i-j]:
          continue
        word = s[i-j:i]
        if word in wordDict:
          dp[i] = True
          break
    print(dp)
    return dp[length]


  def maxlenword(self, wordDict):
    if len(wordDict) == 1:
        # set does not support indexing and slicing. We can iterate set to access its
        # elements, or we can convert it to a list.
        return len(next(iter(wordDict)))
    return len(reduce(lambda x, y : x if len(x) > len(y) else y, wordDict))


if __name__ == "__main__":
  sol = Solution()
  s = "abc"
  word_dict = {"a"}
  print(sol.wordBreak(s, word_dict))

