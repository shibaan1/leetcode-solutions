class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        current_buy = prices[0]
        profit = 0

        for i in range(1 , len(prices)):

            if current_buy > prices[i]:
                current_buy = prices[i]

            x = prices[i]-current_buy

            if profit < x:
                profit = x

        return profit          