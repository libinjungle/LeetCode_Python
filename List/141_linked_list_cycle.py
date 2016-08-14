# Given a linked list, determine if it has a cycle in it.
#
# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
  def hasCycle(self, head):
    """
    if fast catches slow, it has cycle. Otherwise, if fast.next or slow.next is None,
    it has cycle. (Actually only needs to check fast.next is None or not)
    
    :type head: ListNode
    :rtype: bool
    """
    if not head:
      return False
    fast = head
    slow = head
    while slow.next and fast.next and fast.next.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        return True
    return False
