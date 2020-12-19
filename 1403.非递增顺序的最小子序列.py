#
# @lc app=leetcode.cn id=1403 lang=python3
#
# [1403] 非递增顺序的最小子序列
#

from typing import List

# @lc code=start
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums_sum =sum(nums)
        nums.sort(reverse=True)
        result = []
        tmp_sum = 0
        for n in nums:
            result.append(n)
            tmp_sum += n
            if tmp_sum * 2 > nums_sum:
                break
        return result
# @lc code=end

