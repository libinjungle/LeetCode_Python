import collections

class Solution(object):
  def largestRectangleArea(self, heights):
    """
    *** TLE ***
    for each height, find the closest height that is less than it on both left and right side.
    A dictionary to map current height with the index of left closest smaller height and right closest
    smaller height. map[cur_height] = {"left":i, "right":j}
    use a stack to update the store heights that are less than current height. items in stack should be in
    increasing order.
    To get the max area, traverse the dictionary.
    O(n2) for worst case  when heights are in increasing order, since stack will store all previous heights.

    :type heights: List[int]
    :rtype: int
    """
    length = len(heights)
    stack = []
    # create an OrderedDict object.
    rect_map = collections.OrderedDict()
    for i, item in enumerate(heights):
      #print(i, item)
      stack = [inum for inum in stack if inum[1] < item]
      # need to store index as element of key, because heights may have duplicate height.
      rect_map[(i, item)] = {}
      if not stack:
        rect_map[(i, item)]["left"] = -1
      else:
        rect_map[(i, item)]["left"] = stack[-1][0]
      stack.append((i, item))

    stack = []
    # reverse traverse.
    for i in range(length-1, -1, -1):
      stack = [inum for inum in stack if inum[1] < heights[i]]

      if not stack:
        rect_map[(i, heights[i])]["right"] = length
      else:
        rect_map[(i, heights[i])]["right"] = stack[-1][0]
      stack.append((i, heights[i]))

    maxarea = 0
    for iheight in rect_map:
      area = iheight[1] * ((rect_map[iheight]["right"]-1) - (rect_map[iheight]["left"]+1) + 1)
      maxarea = max(maxarea, area)
    return maxarea

  def largestRectangleArea2(self, heights):
    """
    add index of height to stack. for the next adding height, if it is less than the stack peak,
    it is the right time to calculate the area for the stack peak, the width of which is index(next adding height)-
    index(stack peak after pop out current stack)-1. if stack is empty after pop out current stack, the width
    is current index. Update max area after calculate this area.
    if heights are in increasing order, we add a tail height which is -1 so that we can pop out all stack.

    :param heights:
    :return:
    """
    maxarea = 0
    stack = []
    length = len(heights)
    for i in range(length+1):
      curh = heights[i] if i < length else -1
      while stack and curh <= heights[stack[-1]]:
        h = heights[stack.pop()]
        w = i if not stack else i-stack[-1]-1
        area = h * w
        maxarea = max(area, maxarea)
      stack.append(i)
    return maxarea


if __name__ == "__main__":
  sol = Solution()
  heights = [1, 2, 3, 5, 5, 6]
  print(sol.largestRectangleArea2(heights))







