# Reverse a linked list from position m to n. Do it in-place and in one-pass.
#
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
#
# return 1->4->3->2->5->NULL.
#
# Note:
# Given m, n satisfy the following condition:


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
  def reverseList(self, head, diff):
    """
    two iterations.
    :param head:
    :param diff:
    :return:
    """
    if diff == 0:
      return head
    if not head:
      return None
    dummy = None
    prev = dummy
    cur = head
    while diff >= 0:
      next = cur.next
      cur.next = prev
      prev = cur
      cur = next
      diff -= 1
    return prev

  def reverseBetween(self, head, m, n):
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """
    diff = n-m
    if diff == 0:
      return head
    dummy = ListNode(-1)
    dummy.next = head
    count = 1
    cur = head
    preM, nodeM, nodeN, postN = None, None, None, None
    while count <= n and cur:
      if count == m == 1:
        preM = None
        nodeM = cur
      if count == m-1 and m > 1:
        preM = cur
      if count == m and m > 1:
        nodeM = cur

      cur = cur.next
      count += 1

    postN = cur


    if preM is not None:
      preM.next = self.reverseList(nodeM, diff)
    else:
      dummy.next = self.reverseList(nodeM, diff)

    cur = dummy
    while cur.next:
      cur = cur.next
    cur.next = postN

    # the following code does not work. Why?
    # tailnode --> null --> postN

    # cur = dummy.next
    # while cur:
    #   cur = cur.next
    # cur = postN

    return dummy.next


if __name__ == "__main__":
  sol = Solution()
  head = ListNode(1)
  head.next = ListNode(2)
  head.next.next = ListNode(3)
  head.next.next.next = ListNode(4)
  head.next.next.next.next = ListNode(5)
  node = sol.reverseBetween(head, 2, 5)
  while node:
    print(node.val)
    node = node.next









