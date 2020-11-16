#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

from typing import List

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] > 9:
                digits[i] -= 10
                digits[i - 1] += 1
            else:
                break
        if digits[0] > 9:
            digits[0] -= 10
            digits.insert(0, 1)
        return digits
# @lc code=end

