#
# @lc app=leetcode.cn id=970 lang=python3
#
# [970] 强整数
#

from typing import List
import math

# @lc code=start
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        max_i = 1 if x == 1 else math.ceil(math.log(bound, x))
        max_j = 1 if y == 1 else math.ceil(math.log(bound, y))
        result = set()
        for i in range(max_i):
            for j in range(max_j):
                val = x ** i + y ** j
                if val > bound:
                    break
                result.add(x ** i + y ** j)
        return list(result)
        
# @lc code=end

