#
# @lc app=leetcode.cn id=944 lang=python3
#
# [944] 删列造序
#

from typing import List

# @lc code=start
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        n = len(A[0])
        result = 0
        for i in range(n):
            pre = A[0][i]
            for j in range(1, len(A)):
                if A[j][i] >= pre:
                    pre = A[j][i]
                else:
                    result += 1
                    break
        return result

# @lc code=end

