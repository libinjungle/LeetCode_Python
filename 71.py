class Solution(object):
  def simplifyPath(self, path):
    '''
    split path with '/'. In the splitted path list, use stack to update the path
    when traversing the path list.
    T, O(n);
    S, O(n), since need to store parsed element.
    :param path:
    :return:
    '''
    stack = []
    # if path = '/a/b/../', paths = ['', 'a', 'b', '..', '']
    paths = path.split('/')
    for e in paths:
      if e == '.':
        continue
      elif e == '..':
        if len(stack) != 0:
          # remove last element of a list.
          stack.pop()
      elif e == '':
        continue
      else:
        stack.append(e)
    # .join joins elements in list. If stack is empty, '/'.join(stack) will return nothing.
    res = "/" + '/'.join(stack)
    return res

  def simplifyPath2(self, path):
    '''
    use list comprehensions to filter out path.
    :param path:
    :return:
    '''
    stack = []
    p = [e for e in path.split('/') if e != '.' and e != '']
    for place in p:
      if place == '..':
        if len(stack) != 0:
          stack.pop()
      else:
        stack.append(place)

    return '/' + '/'.join(stack)


if __name__ == '__main__':
  sol = Solution()
  path = "/a/b/../"
  res = sol.simplifyPath2(path)
  print res



