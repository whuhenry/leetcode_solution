#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

from typing import List

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        count = len(cost)
        pre = cost[0]
        prepre = 0
        min_cost = 0
        for i in range(1, count):
            min_cost = min(prepre, pre) + cost[i]
            prepre = pre
            pre = min_cost
        return min_cost

        
# @lc code=end

