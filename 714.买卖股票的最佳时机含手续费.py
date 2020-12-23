#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

from typing import List

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) < 2:
            return 0
        
        sell, buy = [0] * len(prices), [0] * len(prices)
        sell[0] = 0
        buy[0] = 0
        for i in range(1, len(prices)):
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i] - prices[i - 1] - fee)
            buy[i] = max(sell[i - 1], buy[i - 1] + prices[i] - prices[i - 1])
        return sell[len(prices) - 1]
        
        
# @lc code=end

s = Solution()
print(s.maxProfit([1, 3, 2, 8, 4, 9], 2))