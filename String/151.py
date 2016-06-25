
'''
Split the string by space. Then reverse the string array.
'''

class solution(object):
  def reverse_words(self, s):
    arr = s.split()
    arrlen = len(arr)
    res = ''
    i = arrlen - 1
    while (i >= 0):
      if (i == 0):
        res += arr[i]
      else:
        res += arr[i] + ' '
      i = i - 1
    return res

class solution2(object):
  ''' join method is used for string. This adds space to each string element.
  '''
  def reverse_words(self, s):
    # [::-1] if to reverse the words list
    return " ".join(s.strip().split()[::-1])

if __name__ == '__main__':
  sol = solution2()
  str = ' hello this is bin li '
  print sol.reverse_words(str)



