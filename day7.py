from typing import List


class Solution:
    def maxProfit(self, prices: List[int]):
        max_gain = 0
        min_cost = prices[0]

        for price in range(len(prices[0:])):
            if min_cost < prices[price]:
                max_gain += prices[price] - min_cost
            min_cost = prices[price]

        return max_gain


prices = [7, 1, 5, 3, 6, 4]
solution = Solution()
print(f"solution result: {solution.maxProfit(prices=prices)}")
