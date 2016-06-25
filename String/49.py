from collections import defaultdict

class solution(object):
  '''
  Given an array of strings, group anagrams together.

  '''
  def groupAnagram(self, arr):
    resList = []
    resList.append([arr[0]])
    for e in arr[1:len(arr)]:
      count = 0
      for i in range(len(resList)):
        if self.isAnagram(e, resList[i][0]):
          resList[i].append(e)
          break
        count += 1
      if count == len(resList):
        # append element as a list
        resList.append([e])
    for e in resList:
      e.sort()
    return resList

  def isAnagram(self, s1, s2):
    dict = {}
    for e in s1:
      if e in dict:
        dict[e] += 1
      else:
        dict[e] = 1

    for e in s2:
      if e in dict and dict[e] >= 1:
        dict[e] -= 1
      elif e in dict and dict[e] <= 0:
        return False
      else:
        return False

    return True

  def group_anagram(self, arr):
    # create a dict to store sorted string and all its anagram mappings
    dict = defaultdict(list)
    for s in arr:
      dict[tuple(sorted(s))].append(s)
    # list comprehension
    return [a for anagram_group in dict.values() if len(anagram_group) > 1 for a in anagram_group]

if __name__ == '__main__':
  sol = solution()
  arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
  print sol.group_anagram(arr)