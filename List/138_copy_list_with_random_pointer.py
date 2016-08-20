# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
  def copyRandomList(self, head):
    """
    :type head: RandomListNode
    :rtype: RandomListNode
    """
    nodes_map = {}
    cur = head
    dummy = RandomListNode(-1)
    copy_cur = dummy

    while cur:
      copy_cur.next = RandomListNode(cur.label)
      copy_cur = copy_cur.next
      nodes_map[cur] = copy_cur
      cur = cur.next

    cur = head
    while cur:
      if not cur.random:
        nodes_map[cur].random = None
      else:
        nodes_map[cur].random = nodes_map[cur.random]
      cur = cur.next
    return dummy.next


