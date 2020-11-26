#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        start = 1
        end = num
        while start <= end:
            center = (start + end) // 2
            center_square = center ** 2
            if center_square == num:
                return True
            elif center_square < num:
                start = center + 1
            else:
                end = center - 1
        return False
# @lc code=end

