#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3的幂
#

# @lc code=start
from typing import ValuesView


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        valid_num = set()
        for i in range(20):
            valid_num.add(3 ** i)
        return n in valid_num
# @lc code=end

