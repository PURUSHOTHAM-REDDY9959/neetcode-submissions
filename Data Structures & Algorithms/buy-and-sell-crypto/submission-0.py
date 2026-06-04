class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')   # very large value
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price   # better buying price found
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)

        return max_profit
