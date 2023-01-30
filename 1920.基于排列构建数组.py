#
# @lc app=leetcode.cn id=1920 lang=python3
#
# [1920] 基于排列构建数组
#

from typing import List

# @lc code=start
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        for i in range(len(nums)):
            result[i] = nums[nums[i]]
        return result
# @lc code=end

