class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit


# Test cases
prices = [7, 1, 5, 3, 6, 4]
# prices = [1, 2, 3, 4, 5]

sol = Solution()
response = sol.maxProfit(prices)
print(response)
