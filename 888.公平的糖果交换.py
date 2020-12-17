#
# @lc app=leetcode.cn id=888 lang=python3
#
# [888] 公平的糖果交换
#

from typing import List

# @lc code=start
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sumA = sum(A)
        sumB = sum(B)
        Sb = set(B)

        for a in A:
            b = (2 * a + sumB - sumA) // 2
            if b in Sb:
                return [a, b]
        
# @lc code=end

