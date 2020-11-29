#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续1的个数
#

from typing import List

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        cur = 0
        for num in nums:
            if num == 1:
                cur += 1
                result = max(cur, result)
            else:
                cur = 0
        return result
# @lc code=end

