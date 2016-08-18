# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
  def partition(self, head, x):
    """
    pointer i, j
    when current node >= x, just move j
    when current node < x, advance j and change i.next
      there are two scenerios when move i,
      1) if nodei.next == nodej, advance nodei
      2) if nodei.next != nodej, make nodei.next = nodej and move other pointers
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """
    if not head:
      return None
    dummy = ListNode(-1)
    dummy.next = head
    cur = head

    nodei, nodej = dummy, cur
    prev = dummy
    while nodej:
      if nodej.val < x:
        if nodei.next == nodej:
          nodei = nodei.next
        else:
          temp = nodej.next
          nexti = nodei.next
          nodei.next = nodej
          nodej.next = nexti
          prev.next = temp
          nodei = nodei.next

      prev = nodej
      nodej = nodej.next
    return dummy.next


if __name__ == "__main__":
  sol = Solution()
  head = ListNode(1)
  head.next = ListNode(4)
  head.next.next = ListNode(2)
  head.next.next.next = ListNode(3)
  head.next.next.next.next = ListNode(5)
  head.next.next.next.next.next = ListNode(2)

  node = sol.partition(head, 9)
  while node:
    print(node.val)
    node = node.next


