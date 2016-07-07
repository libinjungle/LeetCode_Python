class Solution(object):
  def rotate(self, nums, k):
    """
    "三步翻转法".
    in-place solution
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    def reverse(nums, left, right):
      while left < right:
        tmp = nums[left]
        nums[left] = nums[right]
        nums[right] = tmp
        left += 1
        right -= 1

    length = len(nums)
    steps = k % length
    reverse(nums, 0, length-steps-1)
    reverse(nums, length-steps, length-1)
    reverse(nums, 0, length-1)

if __name__ == "__main__":
  sol = Solution()
  nums = [1, 2, 3, 4, 5, 6, 7]
  k = 14
  print sol.rotate(nums, k)