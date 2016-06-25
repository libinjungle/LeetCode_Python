import sys

class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        for word1 equals to word2 case, first sort the index list that has
        word1 and then do one pass do get the shortest distance.
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1 = [i for i in xrange(len(words)) if word1 == words[i]]
        if word1 == word2:
            sorted_indexes = sorted(w1)
            # python's way of Integer.MAX_VALUE
            shortest = sys.maxint
            for i in xrange(len(sorted_indexes)-1):
                d = abs(sorted_indexes[i+1] - sorted_indexes[i])
                if d < shortest:
                    shortest = d
            return shortest
        w2 = [i for i in xrange(len(words)) if word2 == words[i]]
        return min([abs(a-b) for a in w1 for b in w2])