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
    rect_map = collections.OrderedDict()
    for i, item in enumerate(heights):
      #print(i, item)
      stack = [inum for inum in stack if inum[1] < item]

      rect_map[(i, str(item))] = {}
      if not stack:
        rect_map[(i, str(item))]["left"] = -1
      else:
        rect_map[(i, str(item))]["left"] = stack[-1][0]
      stack.append((i, item))
    # print(rect_map)

    stack = []
    for i in range(length-1, -1, -1):
      stack = [inum for inum in stack if inum[1] < heights[i]]

      if not stack:
        rect_map[(i, str(heights[i]))]["right"] = length
      else:
        rect_map[(i, str(heights[i]))]["right"] = stack[-1][0]
      stack.append((i, heights[i]))

    print(rect_map)

    maxarea = 0
    for iheight in rect_map:
      area = int(iheight[1]) * ((rect_map[iheight]["right"]-1) - (rect_map[iheight]["left"]+1) + 1)
      maxarea = max(maxarea, area)
    return maxarea


if __name__ == "__main__":
  sol = Solution()
  heights = [2, 5, 1, 1, 2, 1]
  print(sol.largestRectangleArea(heights))







