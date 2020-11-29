#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

from typing import List

# @lc code=start
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        result = []
        src_r = len(nums)
        src_c = len(nums[0])
        if src_c * src_r != r * c:
            return nums
        
        src_i = 0
        src_j = 0
        for i in range(r):
            line = []
            for j in range(c):
                line.append(nums[src_i][src_j])
                src_j += 1
                if src_j >= src_c:
                    src_j = 0
                    src_i += 1
            result.append(line)
        return result
# @lc code=end

