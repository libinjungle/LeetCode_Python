class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        brutal-force
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
          return 0
        i, j, k = 0, 1, 2
        length = len(nums)
        count = 0
        for i in range(length-2):
          for j in range(i+1, length-1):
            for k in range(j+1, length):
              if nums[i]+nums[j]+nums[k] < target:
                count += 1
        return count

    def threeSumSmaller2(self, nums, target):
      """
      to make it O(n2), either through extra memory or sort the array first
      This case is to sort array. and fix one index and move the other two indexes.
      :param nums:
      :param target:
      :return:
      """
      count = 0
      length = len(nums)
      if length < 3:
        return 0
      nums.sort()

      for i in range(length-2):
        left, right = i+1, length-1
        while left < right:
          if nums[i]+nums[left]+nums[right] >= target:
            right -= 1
          elif nums[i]+nums[left]+nums[right] < target:
            count += right - left
            left += 1
      return count


if __name__ == "__main__":
  sol = Solution()
  nums = [1,-2,4,6,8]
  target = 10
  print sol.threeSumSmaller(nums, target)