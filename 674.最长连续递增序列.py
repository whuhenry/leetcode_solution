#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

from typing import List

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        result = 0
        cur = 0
        for i in range(len(nums)):
            if i > 0:
                if nums[i] > nums[i - 1]:
                    cur += 1
                else:
                    result = max(result, cur)
                    cur = 0
            else:
                cur = 1
        return max(result, cur)
# @lc code=end

