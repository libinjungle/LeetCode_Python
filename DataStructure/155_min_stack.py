class MinStack(object):
  """
  use two stacks, one is the original stack, another is the minstack.
  when push new item, we need to maintain that the top element on minstack
  is always the minimum. To achieve that, we always push the minimum item
  on minstack.
  """
  def __init__(self):
    self._stack = []
    self._minstack = []

  def push(self, x):
    self._stack.append(x)
    if len(self._minstack) == 0:
      self._minstack.append(x)
    else:
      self._minstack.append(min(x, self._minstack[-1]))

  def pop(self):
    self._minstack.pop()
    return self._stack.pop()

  def top(self):
    return self._stack[-1]

  def getMin(self):
    return self._minstack[-1]


if __name__ == "__main__":
  stack = MinStack()
  stack.push(1)
  stack.push(7)
  stack.push(6)
  print(stack.getMin())
  print(stack.pop())


