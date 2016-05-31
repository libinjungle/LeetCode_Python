class solution(object):
  '''
  Given a digit string, return all possible letter combinations that the number could represent.
  '''
  def letterCombinations(self, digits):
    '''
    each element in the returned list represents the input digits.
    parse digit one by one. Store corresponding string for all parsed digits.
    :param digits: digits string, '123'
    :return:
    '''
    # dict hold digit to string mapping
    mappings = {
      '2':'abc',
      '3':'def',
      '4':'ghi',
      '5':'jkl',
      '6':'mno',
      '7':'pqrs',
      '8':'tuv',
      '9':'wxyz'
    }

    prev = ['']
    for d in digits:
      # create new results when adding new digit
      tmp = []
      for x in prev:
        for y in mappings[d]:
          tmp.append(x+y)

      prev = tmp

    return prev

if __name__ == '__main__':
  sol = solution()
  digits = '234'
  print sol.letterCombinations(digits)