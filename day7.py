from typing import List


class Solution:
    def maxProfit(self, prices: List[int]):
        max_gain = 0
        min_cost = prices[0]

        for price in prices[1:]:
            if price >= min_cost:
                max_gain = max(max_gain, price - min_cost)
            else:
                min_cost = min(min_cost, price)
        return max_gain


prices = [7, 1, 5, 3, 6, 4]
solution = Solution()
print(f"solution result: {solution.maxProfit(prices=prices)}")
