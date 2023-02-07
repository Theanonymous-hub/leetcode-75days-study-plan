class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying_price =0
        selling_price =0
        max_profit = 0
        while selling_price<len(prices):
            if prices[selling_price]>prices[buying_price]:
                profit = prices[selling_price] - prices[buying_price]
                if profit > max_profit:
                    max_profit =profit
            else:
                buying_price = selling_price
            selling_price+=1
        return max_profit
        
