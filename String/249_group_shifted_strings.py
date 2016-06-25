class Solution(object):
  '''
  normalize string according to the first character.
  map normalized string to original string list.
  sort map values
  '''
  def group_shifted_string(self, slist):
    dic = {}
    for s in slist:
      norm = self.normalize(s)
      if norm not in dic.keys():
        # can not use append because norm does not exist yet.
        # dic[norm].append(s)

        # append a list contains one string
        dic[norm] = [s]
      else:
        self.insert_to_list(dic[norm], s)

    return [dic[norm] for norm in dic.keys()]


  def normalize(self, s):
      nlist = [(ord(c)-ord(s[0]))%26 for c in s]
      return tuple(nlist)

  def insert_to_list(self, slist, s):
      '''
      insert s into the correct order.
      '''
      i = 0
      # use while loop when needs to check index.
      while i < len(slist):
        # find the position
        if ord(slist[i][0]) > ord(s[0]):
          slist[:] = slist[:i] + [s] + slist[i:]
          break
        else:
          i += 1

        if i == len(slist):
          slist.append(s)
          break

if __name__ == "__main__":
  sol = Solution()
  slist = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
  print sol.group_shifted_string(slist)















