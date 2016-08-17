class ListNode(object):
  def __init__(self, val):
    self.val = val
    self.next = None

class Solution(object):
  def reverseList(self, head):
    # pay attention when initialization. Not every case initialize like this way
    dummy = None
    prev = dummy
    cur = head
    while cur:
      next = cur.next
      cur.next = prev
      prev = cur
      cur = next
    return prev
