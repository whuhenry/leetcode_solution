#
# @lc app=leetcode.cn id=1769 lang=python3
#
# [1769] 移动所有球到每个盒子所需的最小操作数
#

from typing import List

# @lc code=start
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left = [0] * len(boxes)
        right = [0] * len(boxes)
        count = 0
        for i in range(1, len(boxes)):
            if boxes[i - 1] == '1':
                count += 1
            left[i] = left[i - 1] + count
        
        count = 0
        for i in range(len(boxes) - 2, -1, -1):
            if boxes[i + 1] == '1':
                count += 1
            right[i] = right[i + 1] + count
        
        result = [0] * len(boxes)
        for i in range(len(boxes)):
            result[i] = left[i] + right[i]
        
        return result
# @lc code=end

