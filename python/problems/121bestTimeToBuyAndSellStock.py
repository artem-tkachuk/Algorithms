class Solution:
    # O(n^2) time | O(1) space
    def maxProfitBruteForce(self, prices: list[int]) -> int:
        n = len(prices)

        max_profit = 0

        for i in range(n):
            for j in range(i + 1, n):
                curr_profit = prices[j] - prices[j]
                if curr_profit > max_profit:
                    max_profit = curr_profit
        
        return max_profit

    # O(n) time | O(1) space
    def maxProfitLinear(self, prices: list[int]) -> int:
        buyingPrice = float('inf')
        max_profit = 0

        for currPrice in prices:
            if currPrice > buyingPrice:
                curr_profit = currPrice - buyingPrice
                max_profit = max(curr_profit, max_profit)
            else:
                buyingPrice = currPrice

        return max_profit