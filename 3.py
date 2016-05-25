class solution(object):
  '''
  go over the string one character by one character.
  use a hashtable for parsed characters and indexes. When parsing a new char,
  check if this char is already in hashtable. If yes, update the starting index for
  next run. If not, store character and its index.
  '''

  def lenOfLongestSubstring(self, s):
    maxLength = start = 0
    parsedChar = {}

    for i in range(len(s)):
      if s[i] in parsedChar and start <= parsedChar[s[i]]:
        start = parsedChar[s[i]] + 1
      else:
        maxLength = max(maxLength, i-start+1)

      parsedChar[s[i]] = i

    return maxLength

if __name__ == '__main__':
  sol = solution()
  str = "abcabcbbefghjkl"
  print sol.lenOfLongestSubstring(str)



