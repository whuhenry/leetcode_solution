#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        valid_nums = set()
        for i in range(16):
            valid_nums.add(4 ** i)
        return n in valid_nums
# @lc code=end

