#
# @lc app=leetcode.cn id=1598 lang=python3
#
# [1598] 文件夹操作日志搜集器
#

from typing import List

# @lc code=start
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for item in logs:
            if item == '../':
                if stack:
                    stack.pop()
            elif item == './':
                continue
            else:
                stack.append(item)
        return len(stack)
# @lc code=end

