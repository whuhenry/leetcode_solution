#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 字符的最短距离
#

from typing import List

# @lc code=start
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        pre = -1
        result = [len(S)] * len(S)
        for i, ch in enumerate(S):
            if ch == C:
                pre = i
            if pre != -1:
                result[i] = min(result[i], i -  pre)
        
        pre = -1
        len_s = len(S)
        for i, ch in enumerate(S[::-1]):
            if ch == C:
                pre = i
            if pre != -1:
                result[len_s - i - 1] = min(result[len_s - i - 1], i -  pre)

        return result
        
# @lc code=end

s = Solution()
print(s.shortestToChar("loveleetcode", 'e'))