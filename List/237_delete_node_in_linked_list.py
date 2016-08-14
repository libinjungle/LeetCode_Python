# Write a function to delete a node (except the tail) in a singly linked list,
# given only access to that node.
#
# Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3,
# the linked list should become 1 -> 2 -> 4 after calling your function.

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
  def deleteNode(self, node):
    """
    since we only have access to the node to be deleted, means we don't have access to the previous
    node. we can move the data of next node and delete next node by moving the pointer
    *except the tail

    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    if not node:
      return
    node.val = node.next.val
    node.next = node.next.next



