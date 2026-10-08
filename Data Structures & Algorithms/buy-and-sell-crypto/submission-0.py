class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_min = float("inf")
        max_profit = 0
        for sell_value in prices:
            left_min = min(left_min, sell_value)
            if sell_value > left_min:
                max_profit = max(
                    max_profit, sell_value - left_min
                )
        return max_profit
        