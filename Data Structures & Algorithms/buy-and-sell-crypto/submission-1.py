class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_Profit = 0
        while(r < len(prices)):
            if prices[l] < prices[r]:
                max_Profit = max(max_Profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return max_Profit
