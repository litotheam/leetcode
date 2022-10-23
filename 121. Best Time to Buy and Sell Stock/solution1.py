class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day = 0
        sell_day = 1
        max_profit = 0
        end_day = len(prices)-1
        while(sell_day <= end_day):
            profit = prices[sell_day] - prices[buy_day]
            if profit <= 0:
                buy_day = sell_day
                sell_day += 1
            else:
                if profit > max_profit:
                    max_profit = profit
                sell_day += 1

        return max_profit