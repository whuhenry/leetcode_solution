#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

from typing import List

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_sum = sum(nums)
        count = len(nums)
        delta = count * (count + 1) // 2 - nums_sum
        nums.sort()
        for i in range(1, count):
            if nums[i] == nums[i - 1]:
                return [nums[i], nums[i] + delta]
# @lc code=end

