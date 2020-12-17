#
# @lc app=leetcode.cn id=989 lang=python3
#
# [989] 数组形式的整数加法
#

from typing import List

# @lc code=start
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A = A[::-1]
        A[0] += K
        idx = 0
        while A[idx] > 9:
            if idx == len(A) - 1:
                A.append(A[idx] // 10)
            else:
                A[idx + 1] += A[idx] // 10
            A[idx] = A[idx] % 10
            idx += 1
        return A[::-1]
        
# @lc code=end

