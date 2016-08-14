
class Solution(object):
  def maxProfit(self, prices):
    """
    DP solution

    state
    -----
    f[i] is the maximum profit in the previous i prices.

    initial
    -------
    f[0], f[1] = 0, 0

    function
    --------
    f[i] = max(f[i-1], current price - min price if current price > min price)

    return
    ------
    max(f), not f[length], there is an edge case that the min price is the last price.

    :type prices: List[int]
    :rtype: int
    """
    length = len(prices)
    if length <= 1:
      return 0
    f = [0]*(length+1)
    f[0], f[1] = 0, 0
    minprice = prices[0]
    for i in range(2, length+1):
      if minprice > prices[i-1]:
        minprice = prices[i-1]
        continue
      f[i] = max(prices[i-1] - minprice, f[i-1])
    # edge case: the min price is the last price.
    return max(f)


  def maxProfit2(self, prices):
    """
    Greedy solution
    :param prices:
    :return:
    """
    # float('inf') represents an infinite large number.
    maxprofit, minprice = 0, float('inf')
    for price in prices:
      minprice = min(price, minprice)
      maxprofit = max(maxprofit, price-minprice)
    return maxprofit


if __name__ == "__main__":
  sol = Solution()
  prices = [2,4,6,7,4]
  print(sol.maxProfit2(prices))
