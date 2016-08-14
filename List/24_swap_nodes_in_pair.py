# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution(object):
  def swapPairs(self, head):
    """
    use dummy node as the current pointer. change pointer from left to right.
    record cur.next and cur.next.next when they are not None.

    :type head: ListNode
    :rtype: ListNode
    """
    dummy = ListNode(-1)
    dummy.next = head
    cur = dummy
    while cur.next and cur.next.next:
      first = cur.next
      second = cur.next.next
      cur.next = second
      first.next = second.next
      second.next = first
      cur = first
    return dummy.next


if __name__ == "__main__":
  sol = Solution()
  head = ListNode(1)
  head.next = ListNode(2)
  head.next.next = ListNode(3)
  head.next.next.next = ListNode(4)
  node = sol.swapPairs(head)
  while node:
    print(node.val)
    node = node.next
