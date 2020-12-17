#
# @lc app=leetcode.cn id=1005 lang=python3
#
# [1005] K 次取反后最大化的数组和
#

from typing import List

# @lc code=start
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        result = sum(A)
        A.sort()
        for i, a in enumerate(A):
            if a < 0 and K > 0:
                A[i] = -a
                K -= 1
            else:
                break
        minA = min(A)
        tmp = 1 if K % 2 == 0 else -1
        result = sum(A) - minA + tmp * minA
        
        return result
# @lc code=end

s = Solution()
s.largestSumAfterKNegations([-8,3,-5,-3,-5,-2], 6)