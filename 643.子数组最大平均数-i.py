#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

from typing import List

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = 0
        num_sum = 0
        for i in range(k):
            num_sum += nums[i]
        result = num_sum
        for i in range(k, len(nums)):
            num_sum += nums[i] - nums[i - k]
            result = max(result, num_sum)
        return result / k
# @lc code=end

