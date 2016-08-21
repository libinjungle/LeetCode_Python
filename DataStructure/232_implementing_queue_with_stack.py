class Queue(object):
  """
  use two stacks. for push, push onto the second stack. for pop, if first stack is empty,
  push items from the second stack, and then pop out item. Do the same for peek.
  for empty check, return True if both stacks are empty.

  """
  def __init__(self):
    self._stack1 = []
    self._stack2 = []

  def stack2Tostack1(self):
    while self._stack2:
      self._stack1.append(self._stack2.pop())

  def push(self, x):
    self._stack2.append(x)

  def pop(self):
    if not self._stack1:
      self.stack2Tostack1()
    return self._stack1.pop()

  def peek(self):
    if not self._stack1:
      self.stack2Tostack1()
    return self._stack1[-1]

  def empty(self):
    return not self._stack1 and not self._stack2


