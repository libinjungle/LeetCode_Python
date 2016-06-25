class solution(object):
  def shortestDistance(self, words, word1, word2):
    '''
    assuming all words are lower case.

    :param words: List[str]
    :param word1: str
    :param word2: str
    :return:
    '''
    word_dict = {}
    for i in range(len(words)):
      if words[i] not in word_dict:
        word_dict[words[i]] = []
      word_dict[words[i]].append(i)

    indexs_1 = word_dict[word1]
    indexs_2 = word_dict[word2]
    shortest_dist = len(words) - 1
    for i in indexs_1:
      for j in indexs_2:
        if abs(j-i) < shortest_dist:
          shortest_dist = abs(j-i)
    return shortest_dist

  def shortestDistance2(self, words, word1, word2):
    '''
    get index of each occurrence of word1 and word2.
    calculate the shortest distance.
    :return:
    '''
    w1 = [i for i in xrange(len(words)) if words[i] == word1]
    w2 = [i for i in xrange(len(words)) if words[i] == word2]
    return min([abs(a-b) for a in w1 for b in w2])


  def to_upper(self, words):
    # str is a string object.
    return map(str.upper, words)

  def to_lower(self, words):
    return map(str.lower, words)


if __name__ == "__main__":
  sol = solution()
  words = ["practice", "makes", "perfect", "coding", "makes"]
  print sol.to_upper(words)
  print sol.shortestDistance(words, "makes", "perfect")
