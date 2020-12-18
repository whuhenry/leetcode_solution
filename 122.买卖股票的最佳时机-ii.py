#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

from typing import List

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        stack = []
        for price in prices:
            if 0 == len(stack) or stack[-1] <= price:
                stack.append(price)
            else:
                if len(stack) > 1:
                    result += stack[-1] - stack[0]
                stack = [price]
        if len(stack) > 1:
            result += stack[-1] - stack[0]
        return result
# @lc code=end

s = Solution()
print(s.maxProfit([7,6,4,3,1]))