#
# @lc app=leetcode.cn id=2006 lang=python3
#
# [2006] 差的绝对值为 K 的数对数目
#

from typing import List

# @lc code=start
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) == k:
                    result += 1

        return result
# @lc code=end

