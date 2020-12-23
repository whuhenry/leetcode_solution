#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

from typing import List

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while(start <= end):
            center = (start + end) // 2
            if nums[center] == target:
                return center
            elif nums[center] < target:
                start = center + 1
            else:
                end = center - 1
        return end + 1
# @lc code=end

