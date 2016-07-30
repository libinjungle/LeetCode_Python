class Solution(object):
  def largestDivisibleSubset(self, nums):
    """
    Time Limit Exceeded.
    each cell in dp list stores the matched sublists for all previous nums plus current num.
    :type nums: List[int]
    :rtype: List[int]
    """

    length = len(nums)
    dp = [[] for _ in range(length)]
    dp[0] = [[nums[0]]]
    for i in range(1, length):
      for sub in dp[i-1]:
        compatible =  True
        for num in sub:
          if (nums[i] % num != 0 and num % nums[i] != 0):
            dp[i].append(sub)
            dp[i].append([nums[i]])
            compatible = False
            break
        if compatible == True:
          dp[i].append(sub + [nums[i]])
    return max(dp[length-1], key=len)


  def largestDivisibleSubset2(self, nums):
    """
    dp is a dict maps current num with its largest subset.
    Nice solution by stefan. A very flexible dp solution.
    sort the list up front. As the list is sorted, for traverse through dp,
    only dp[largest divisor] is added with current num.
    base case: dp[-1] = set(), otherwise, max function will run into problem.(max arg is empty sequence)
    :param nums:
    :return:
    """

    dp = {-1:set()}
    nums = sorted(nums)
    for k in nums:
      dp[k] = max((dp[m] for m in dp if k % m == 0), key=len) | {k}
    return max(dp.values(), key=len)


if __name__ == "__main__":
  sol = Solution()
  nums = [2,3,6,9,12]
  print(sol.largestDivisibleSubset(nums))











