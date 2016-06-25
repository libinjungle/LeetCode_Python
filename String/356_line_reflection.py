class Solution(object):
  def isReflected(self, points):
    """
    Group points by y axis. For each group which has the same y axis, take the
    average of points based on x axis. Let's call it avg_x. Considering only x axis,
    If the sum of offsets with average is not zero for a group, it is not reflected.
    If avg_x is different for two groups, it is not reflected.
    time: O(n) for group points. O(n) for check if it is reflected.
    space: O(n) for a dict to store grouped points.

    :type points: List[List[int]]
    :rtype: bool
    """
    # points grouped by y axis
    DEBUG = False
    group = self.group_points(points)
    prev_avg = 0

    for i in range(len(group)):
      xsum = 0
      for point in group[i]:
        xsum += point[0]
      avg = float(xsum)/len(group[i])
      if DEBUG:
        print avg

      offset = 0
      for point in group[i]:
        offset += point[0] - avg
      if DEBUG:
        print offset

      if offset != 0:
        return False
      if i != 0:
        if avg != prev_avg:
          return False
      prev_avg = avg

    return True

  def isReflected2(self, points):
    '''
    reflect points by repalcing x with maxX+minX-x. Then see if they are same points
    :param points:
    :return:
    '''
    if not points:
      return True
    X = max(points)[0]+min(points)[0]
    # List has order. {} means set. Note that set = {} is not a set, it is an dict.
    return {(x, y) for x, y in points} == {(X-x, y) for x, y in points}

  def group_points(self, points):
    '''
    group points based on y axis.
    :param points: List[List[int]]
    :return:
    '''
    group = {}
    for point in points:
      if point[1] not in group:
        group[point[1]] = []
        group[point[1]].append(point)
      else:
        group[point[1]].append(point)

    return group.values()


if __name__ == '__main__':
  sol = Solution()
  points = [[1,2], [2,3], [3,2], [4,3], [2,6], [4,6]]
  points2 = [[2,3], [4,3], [2,6], [4,6]]
  points3 = [[2,3], [2,5]]
  # only one group
  points3 = [[0,0],[1,0],[3,0]]
  points4 = [[0,0],[1,0]]

  print sol.group_points(points4)
  print sol.isReflected(points4)
  print sorted(points)
  print min(points), max(points)


