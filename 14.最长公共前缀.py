#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

from typing import List

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ''
        result = ''
        for i in range(len(strs[0])):
            flag = True
            for j in range(1, n):
                if i >= len(strs[j]):
                    flag = False
                    break
                if strs[j][i] != strs[0][i]:
                    flag = False
                    break
            if flag:
                result += strs[0][i]
            else:
                break
        return result
# @lc code=end

