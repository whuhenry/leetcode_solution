#
# @lc app=leetcode.cn id=1304 lang=python3
#
# [1304] 和为零的N个唯一整数
#

from typing import List

# @lc code=start
class Solution:
    def sumZero(self, n: int) -> List[int]:
        start = -(n // 2)
        end = n // 2
        result = []
        for i in range(start, 0):
            result.append(i)
        for i in range(1, end + 1):
            result.append(i)
        if n % 2 == 1:
            result.append(0)
        return result

# @lc code=end

