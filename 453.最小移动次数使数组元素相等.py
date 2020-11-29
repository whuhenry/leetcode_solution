#
# @lc app=leetcode.cn id=453 lang=python3
#
# [453] 最小移动次数使数组元素相等
#

from typing import List

# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_ele = min(nums)
        result = 0
        for num in nums:
            result += num - min_ele
        return result
# @lc code=end

