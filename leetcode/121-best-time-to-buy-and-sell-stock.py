class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_point = 0
        min_point = 0
        curr_max_profit = 0
        for time_point, value in enumerate(prices):
            if value < prices[min_point]:
                min_point = time_point
            if max_point < min_point:
                max_point = time_point
            if value > prices[max_point]:
                max_point = time_point
            if curr_max_profit < prices[max_point] - prices[min_point]:
                curr_max_profit = prices[max_point] - prices[min_point]
        return curr_max_profit