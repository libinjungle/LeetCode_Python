class WordDistance(object):
    '''
    follow-up of 243 shortest word distance.
    use a dictionary to store index of all words.
    '''
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.word_dict = {}
        for i in range(len(words)):
            if words[i] not in self.word_dict:
                self.word_dict[words[i]] = []
            self.word_dict[words[i]].append(i)

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1 = self.word_dict[word1]
        w2 = self.word_dict[word2]
        return min([abs(a-b) for a in w1 for b in w2])



# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")