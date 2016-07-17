import collections
import heapq

class Twitter(object):

  def __init__(self):
    """
    Initialize your data structure here.
    timestamp for order tweets
    userinfo: key/value = uid/(deque to store tweets, [followee])
    """

    self.timestamp = 0
    self.userinfo = {}

  def postTweet(self, userId, tweetId):
    """
    Compose a new tweet.
    :type userId: int
    :type tweetId: int
    :rtype: void
    """

    self.timestamp += 1

    if userId not in self.userinfo:
      self.userinfo[userId] = collections.deque(), {userId}
    # remove outdated tweet.
    if len(self.userinfo[userId][0]) == 10:
      self.userinfo[userId][0].pop()
    self.userinfo[userId][0].appendleft((-self.timestamp, tweetId))


  def getNewsFeed(self, userId):
    """
    Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.

    use heapq(PriorityQueue) to order tweets that all followee has. Extract the first 10.

    :type userId: int
    :rtype: List[int]
    """

    if userId not in self.userinfo:
      return []
    heap = []
    for fid in self.userinfo[userId][1]:
      if fid in self.userinfo:
        for tweet in self.userinfo[fid][0]:
          # put tweet on heap.
          heapq.heappush(heap, tweet)
    hlen = len(heap)
    res = []
    # edge case: the number of tweets may be less than 10.
    while len(res) < min(hlen, 10):
      res.append(heapq.heappop(heap)[1])
    return res


  def follow(self, followerId, followeeId):
    """
    Follower follows a followee. If the operation is invalid, it should be a no-op.
    :type followerId: int
    :type followeeId: int
    :rtype: void
    """

    if followerId not in self.userinfo:
      self.userinfo[followerId] = collections.deque(), {followerId}
    self.userinfo[followerId][1].add(followeeId)


  def unfollow(self, followerId, followeeId):
    """
    Follower unfollows a followee. If the operation is invalid, it should be a no-op.
    :type followerId: int
    :type followeeId: int
    :rtype: void
    """

    if followerId not in self.userinfo:
      return

    # if unfollow herself, don't need to discard.
    if followerId != followeeId:
      self.userinfo[followerId][1].discard(followeeId)

if __name__ == "__main__":
  obj = Twitter()
  obj.postTweet(1, 21)
  obj.postTweet(2, 22)
  obj.follow(1, 2)
  obj.postTweet(1, 23)
  obj.postTweet(2, 33)
  recent_tweets = obj.getNewsFeed(1)
  print(recent_tweets)
