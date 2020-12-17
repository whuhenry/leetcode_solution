#
# @lc app=leetcode.cn id=1408 lang=python3
#
# [1408] 数组中的字符串匹配
#

from typing import List

# @lc code=start
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        result = []
        for i in range(n):
            for j in range(n):
                if i != j and words[i] in words[j]:
                    result.append(words[i])
                    break
        return result
# @lc code=end

