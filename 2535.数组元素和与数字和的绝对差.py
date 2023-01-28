#
# @lc app=leetcode.cn id=2535 lang=python3
#
# [2535] 数组元素和与数字和的绝对差
#

from typing import List

# @lc code=start
class Solution:

    def digit_sum(self, num):
        result = 0
        while num > 0:
            result += num % 10
            num = num // 10
        return result

    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        return abs(sum(map(self.digit_sum, nums)) - element_sum)

# @lc code=end

