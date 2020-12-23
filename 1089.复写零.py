#
# @lc app=leetcode.cn id=1089 lang=python3
#
# [1089] 复写零
#

from typing import List

# @lc code=start
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        idx = 0
        len_a = len(arr)
        while idx < len(arr):
            if arr[idx] == 0:
                arr.insert(idx, 0)
                idx += 2
                arr.pop()
            else:
                idx += 1
# @lc code=end

