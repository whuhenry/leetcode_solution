#
# @lc app=leetcode.cn id=830 lang=python3
#
# [830] 较大分组的位置
#

from typing import List

# @lc code=start
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        head = 0
        tail = 0
        result = []
        while head < len(s):
            tail = head + 1
            while tail < len(s) and s[tail] == s[head]:
                tail += 1
            if tail - head >= 3:
                result.append([head, tail - 1])
            head = tail
        return result
# @lc code=end

