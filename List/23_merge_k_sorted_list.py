import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
  def mergeKLists(self, lists):
    """
    divide and conquer
    base case: when lists size is 0, return None; when lists size is 1, return lists[0]
    time: O(nKlogK), K is the size of lists, n is the length of a list

    :type lists: List[ListNode]
    :rtype: ListNode
    """
    size = len(lists)
    if size == 0:
      return None
    #
    if size == 1:
      return lists[0]
    middle = size/2
    firsthalf = self.mergeKLists(lists[0:middle])
    secondhalf = self.mergeKLists(lists[middle:size])
    return self.merge(firsthalf, secondhalf)


  def merge(self, head1, head2):
    dummy = ListNode(-1)
    cur = dummy
    while head1 and head2:
      if head1.val <= head2.val:
        cur.next = head1
        head1 = head1.next
      else:
        cur.next = head2
        head2 = head2.next
      cur = cur.next
    if head1:
      cur.next = head1
    if head2:
      cur.next = head2
    return dummy.next


  def mergeKlists2(self, lists):
    """
    use heap queue to sort the added nodes. the popped out node will be appended to resultlist.
    node there may be None node in lists. so don't push None node.
    since heapq can only sort based on the first element of tuple, a high level object is created
    to enable sort on ListNode.val
    time: O(nKlogK), K is the size of lists

    :param lists: List[ListNode]
    :return:
    """
    class MyHeap(object):
      def __init__(self, initial=None, key=lambda x : x):
        self.key = key
        if initial:
          self._data = [(key(item), item) for item in initial]
          heapq.heapify(self._data)
        else:
          self._data = []

      def push(self, item):
        heapq.heappush(self._data, (self.key(item), item))

      def pop(self):
        return heapq.heappop(self._data)[1]

    initial = None
    key = lambda x : x.val
    h = MyHeap(initial, key)
    for node in lists:
      # edge case: None node
      if node:
        h.push(node)
    print(h._data)

    dummy = ListNode(-1)
    cur = dummy

    # it is h._data that gets popped out, not h.
    while h._data:
      node = h.pop()
      cur.next = node
      if node.next:
        h.push(node.next)
      cur = cur.next
    return dummy.next


if __name__ == "__main__":
  sol = Solution()
  head = ListNode(1)
  head.next = ListNode(2)
  head.next.next = ListNode(4)
  head.next.next.next = ListNode(4)
  head.next.next.next.next = ListNode(5)

  head2 = ListNode(7)
  head2.next = ListNode(8)
  head2.next.next = ListNode(9)

  klists = []
  klists.append(head)
  klists.append(head2)
  # print(klists)


  node = sol.mergeKlists2(klists)
  while node:
    print(node.val)
    node = node.next


