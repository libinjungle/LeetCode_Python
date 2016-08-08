class Solution(object):
  def wiggleMaxLength(self, nums):
    """
    state
    -----
    f[i] is the longest subsequence length of previous i nums

    initial
    -------
    each element of dp array is a tuple that is (longest length, True or False)
    True means current > previous, False means current < previous.
    if current == previous, f[current] = f[previous]

    f[0] = (0, True)
    f[1] = (1, True)
    f[2] = compare nums[1] with nums[0], then create tuple
    f[i] = compare nums[i-1] with nums[i-2], update flag

    :type nums: List[int]
    :rtype: int
    """

    length = len(nums)
    if length <= 1:
      return length
    # True means current num is bigger than previous num.
    f = [(0, True) for _ in range(length+1)]
    f[1] = (1, True)
    if nums[1] - nums[0] > 0:
      f[2] = (2, True)
    elif nums[1] - nums[0] < 0:
      f[2] = (2, False)
    else:
      f[2] = (1, True)
    if length == 2:
      return f[2][0]

    for i in range(3, length+1):
      if f[i-1][1] == True and nums[i-1] - nums[i-2] < 0:
        f[i] = (f[i-1][0] + 1, False)
      elif f[i-1][1] == False and nums[i-1] - nums[i-2] > 0:
        f[i] = (f[i-1][0] + 1, True)
      else:
        f[i] = (f[i-1][0], f[i-1][1])

    return f[length][0]


  def wiggleMaxLength2(self, nums):
    """
    Greedy solution
    according to current stage(bigger or smaller), anticipate next
    stage. Then check if this anticipate meets.
    :param nums:
    :return:
    """
    length = len(nums)
    if length <= 1:
      return length
    big = (nums[1] - nums[0] > 0)
    count = 1
    for i in range(1, length):
      if (big and nums[i] - nums[i-1] > 0) or (not big and nums[i] - nums[i-1] < 0):
        count += 1
        big = (not big)
    return count


if __name__ == "__main__":
  sol = Solution()
  nums = [1,2,3,4,5,6,7,8,9]
  print(sol.wiggleMaxLength2(nums))


