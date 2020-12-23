#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#

from typing import List

# @lc code=start
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = 1
        even = 0
        while odd < len(A) and even < len(A):
            if A[odd] % 2 == 0 and A[even] % 2 == 1:
                A[odd], A[even] = A[even], A[odd]
            else:
                if A[odd] % 2 == 1:
                    odd += 2
                if A[even] % 2 == 0:
                    even += 2
        return A
# @lc code=end

