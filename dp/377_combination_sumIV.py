class Solution(object):
  def combinationSum4(self, nums, target):
    """
    dp[0..target] represents the number of combinations for 0 through target.
    for each index of dp, traverse all nums, if num < index, add dp[index-num] to
    dp[index]. if num == index, add one. if num > index, skip.
    time: O(n2)
    space: O(target)

    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums = sorted(nums)
    # base case is 0
    dp = [0 for _ in range(target+1)]
    length = len(dp)
    for i in range(1, length):
      for num in nums:
        if num > i:
          break
        elif num == i:
          dp[i] += 1
        else:
          dp[i] += dp[i-num]
    return dp[target]


if __name__ == "__main__":
  sol = Solution()
  nums = [1, 2, 3]
  print(sol.combinationSum4(nums, 4))


