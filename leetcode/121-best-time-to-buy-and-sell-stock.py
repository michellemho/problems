class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        for buy_time, buy_price in enumerate(prices):
            for sell_price in prices[buy_time:]:
                profits.append(sell_price - buy_price)
        return max(profits)
