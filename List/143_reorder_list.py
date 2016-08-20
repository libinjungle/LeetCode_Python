# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
  def reorderList(self, head):
    """
    1. find middle node
    2. reverse node after middle node
    3. concat two list
    in place
    
    :type head: ListNode
    :rtype: void Do not return anything, modify head in-place instead.
    """
    if not head:
      return head

    cur = head
    middle = self.find_middle_node(cur)

    middle_next = middle.next
    middle.next = None
    rvs_after_middle = self.reverse_list(middle_next)


    curhead = head
    currvs = rvs_after_middle
    while currvs:
      rvs_next = currvs.next
      cur_next = curhead.next
      curhead.next = currvs
      currvs.next = cur_next
      curhead = cur_next
      currvs = rvs_next
    return head


  def find_middle_node(self, head):
    if not head or not head.next:
      return head
    slow = head
    fast = head.next
    while fast and fast.next:
      fast = fast.next.next
      slow = slow.next
    return slow


  def reverse_list(self, head):
    if not head:
      return head
    prev = None
    while head:
      nextnode = head.next
      head.next = prev
      prev = head
      head = nextnode
    return prev


if __name__ == "__main__":
  sol = Solution()
  head = ListNode(1)
  head.next = ListNode(2)
  head.next.next = ListNode(3)
  head.next.next.next = ListNode(4)
  head.next.next.next.next = ListNode(5)

  head2 = ListNode(1)
  head2.next = ListNode(2)
  head2.next.next = ListNode(3)
  node = sol.reorderList(head2)


  while node:
    print(node.val)
    node = node.next








