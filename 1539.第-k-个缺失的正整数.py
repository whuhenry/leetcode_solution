#
# @lc app=leetcode.cn id=1539 lang=python3
#
# [1539] 第 k 个缺失的正整数
#

from typing import List

# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        mis_count = 0
        arr_ptr = 0
        for i in range(1, 2002):
            if arr_ptr < len(arr) and i == arr[arr_ptr]:
                arr_ptr += 1
            else:
                mis_count += 1
                if mis_count == k:
                    return i

# @lc code=end

