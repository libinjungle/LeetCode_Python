# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

def knows(a, b):
  pass

class Solution(object):
  def findCelebrity(self, n):
    """
    two passes. first pass to get the candidate. second pass to validate if the candidate is real celebrity
    my solution
    O(n) and no extra memory.
    :type n: int
    :rtype: int
    """
    maybe = 0
    for i in range(1, n):
      if knows(maybe, i):
        maybe = i
    for i in range(n):
      if (i != maybe and knows(maybe, i)) or not knows(i, maybe):
        return -1
    return maybe







