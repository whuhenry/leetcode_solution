#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

from typing import List

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        head = 0
        tail = len(nums) - 1

        loc = -1
        start = -1
        end = -1

        while head <= tail:
            center = (head + tail) // 2
            if nums[center] == target:
                loc = center
                break
            elif nums[center] > target:
                tail = center - 1
            else:
                head = center + 1
        
        if loc != -1:
            start = loc
            end = loc
            while start - 1 >= 0  and nums[start - 1] == nums[loc]:
                start -= 1
            while end + 1 <= len(nums) - 1  and nums[end + 1] == nums[loc]:
                end += 1
        return [start, end]
# @lc code=end

