class Solution(object):
  def threeSumClosest(self, nums, target):
    """
    since nums can either be positive or negative, and we need to find the closest combination.
    So we can not break out of loop while updating.
    Idea: sort upfront. if three triplets bigger than target, reduce high index by one. If smaller than
    target, increase low index by one.
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    length = len(nums)
    nums.sort()
    if length < 2:
      raise Exception("nums must have at least three numbers.")
    sum = nums[0]+nums[1]+nums[length-1]
    for i in range(length-2):
      left, right = i+1, length-1
      while left < right:
        localsum = nums[i]+nums[left]+nums[right]
        if localsum > target:
          right -= 1
        elif localsum < target:
          left += 1
        else:
          return localsum
        if abs(localsum-target) < abs(sum-target):
          sum = localsum
    return sum

if __name__ == "__main__":
  sol = Solution()
  nums = [3,2,1,-4]
  print sol.threeSumClosest(nums, 1)


