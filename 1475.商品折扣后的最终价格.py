#
# @lc app=leetcode.cn id=1475 lang=python3
#
# [1475] 商品折扣后的最终价格
#

from typing import List

# @lc code=start
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = prices.copy()
        n = len(prices)
        for i in range(n):
            min_idx = -1
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    min_idx = j
                    break
            if min_idx != -1:
                result[i] -= result[min_idx]
        return result
# @lc code=end

