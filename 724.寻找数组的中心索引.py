#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心索引
#

from typing import List

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        sum_left = 0
        for i, num in enumerate(nums):
            if sum_left == sum_nums - num - sum_left:
                return i
            sum_left += num
        return -1


# @lc code=end

