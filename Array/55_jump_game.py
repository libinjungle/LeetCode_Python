class Solution(object):
  def canJump(self, nums):
    """
    My solution: Too slow
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) == 1:
      return True
    i = nums[0]
    if i == 0: return False
    canjumps = [self.canJump(nums[j:]) for j in range(1, i+1) if j < len(nums)]
    for jump in canjumps:
      if jump == True:
        return True
    return False

  def canJump2(self, nums):
    '''
    one-pass
    when index moves forward, check if current index can be reached by get the previous max moves, which is
    max([prev_index + nums[pre_index])
    :param nums:
    :return:
    '''
    maxmoves = 0
    for i, num in enumerate(nums):
      if maxmoves < i: return False
      if maxmoves < i+num:
        maxmoves = i+num
    return True

if __name__ == "__main__":
  sol = Solution()
  A = [3,2,1,0,4]
  A1 = [0]
  A2 = [0,1]
  A3 = [1,1,1,1,1,1,1,1,1]
  A4 = [1,2,2,6,3,6,1,8,9,4,7,6,5,6,8,2,6,1,3,6,6,6,3,2,4,9,4,5,9,8,2,2,1,6,1,6,2,2,6,1,8,6,8,3,2,8,5,8,0,1,4,8,7,9,0,3,9,4,8,0,2,2,5,5,8,6,3,1,0,2,4,9,8,4,4,2,3,2,2,5,5,9,3,2,8,5,8,9,1,6,2,5,9,9,3,9,7,6,0,7,8,7,8,8,3,5,0]
  print sol.canJump2(A4)


