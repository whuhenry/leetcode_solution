#
# @lc app=leetcode.cn id=1614 lang=python3
#
# [1614] 括号的最大嵌套深度
#

# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        result = 0
        for ch in s:
            if ch == '(':
                stack.append(ch)
                result = max(result, len(stack))
            elif ch == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(ch)
                    result = max(result, len(stack))
        return result
# @lc code=end

