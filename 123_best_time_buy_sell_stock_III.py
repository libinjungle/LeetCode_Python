import sys

class Solution(object):
  def maxProfit(self, prices):
    """
    buy-sell-buy-sell
    can not buy-buy-sell-sell

    max2 = max profit for two transaction
    lowestBuyPrice2 = the lowest buy price that has already counted max profit for the first buy.
                      right after the first trasanction is made, lowestBuyPrice2 will be the timestamp after the sell point.
    max1 = max profit for one transaction
    lowestBuyPrice1 = current lowest price

    :type prices: List[int]
    :rtype: int
    """
    max1, max2 = 0, 0
    lowestBuyPrice1, lowestBuyPrice2 = sys.maxint, sys.maxint
    for price in prices:
      max2 = max(max2, price - lowestBuyPrice2)
      lowestBuyPrice2 = min(lowestBuyPrice2, price - max1)
      max1 = max(max1, price - lowestBuyPrice1)
      lowestBuyPrice1 = min(lowestBuyPrice1, price)
    return max2


if __name__ == "__main__":
  sol = Solution()
  prices = [1,2,4,3,5,7]
  print(sol.maxProfit(prices))




