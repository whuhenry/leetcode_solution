#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, S: str) -> str:
        result = []
        for ch in S:
            if not result:
                result.append(ch)
            else:
                if ch == result[-1]:
                    result.pop()
                else:
                    result.append(ch)
        return ''.join(result)
# @lc code=end

