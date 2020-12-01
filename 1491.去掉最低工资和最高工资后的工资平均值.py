#
# @lc app=leetcode.cn id=1491 lang=python3
#
# [1491] 去掉最低工资和最高工资后的工资平均值
#

from typing import List

# @lc code=start
class Solution:
    def average(self, salary: List[int]) -> float:
        max_s = max(salary)
        min_s = min(salary)
        return (sum(salary) - max_s - min_s) / (len(salary) - 2)
# @lc code=end

