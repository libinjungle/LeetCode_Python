class Codec:
  # CAN NOT WORK FOR MANY TEST CASES
  # def encode(self, strs):
  #   """Encodes a list of strings to a single string.
  #   :type strs: List[str]
  #   :rtype: str
  #   """
  #   res = ''
  #   for i in xrange(len(strs)):
  #     # replace substring
  #     strs[i].replace(' ', '%20')
  #     res = res + strs[i] + '&'
  #   return res
  #
  # def decode(self, s):
  #   """Decodes a single string to a list of strings.
  #
  #   :type s: str
  #   :rtype: List[str]
  #   """
  #   res = []
  #   start = 0
  #   s.replace('&', ' ')
  #   for i in xrange(len(s)):
  #     if s[i] == '&':
  #       res.append(s[start:i])
  #       start = i+1
  #   return res

  def encode(self, strs):
    """Encodes a list of strings to a single string.

    put string length and a space ahead of each string

    :type strs: List[str]
    :rtype: str
    """
    res = ''
    for s in strs:
      res += str(len(s))
      res += ' '
      res += s
    return res

  def decode(self, s):
    '''
    each element is (len' 'str)
    :param s:
    :return:
    '''
    res = []
    length = 0
    size = len(s)
    i = 0
    while i < size:
      if s[i] != ' ':
        length = length*10 + int(s[i])
        i += 1
      else:
        i += 1
        res.append(s[i:i+length])
        i += length
        length = 0

    return res


  def encode2(self, strs):
    return ''.join('%d:' %len(s) + s for s in strs)

  def decode2(self, s):
    res = []
    i = 0
    while i < len(s):
      j = s.find(':', i)
      i = j+1+int(s[i:j])
      res.append(s[j+1:i])
    return res


if __name__ == '__main__':
  codec = Codec()
  str = ['hello ', 'this is bin']
  print codec.decode2(codec.encode2(str))