#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

from typing import List

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_idx = 0
        s_idx = 0
        result = 0
        while g_idx < len(g) and s_idx < len(s):
            if g[g_idx] <= s[s_idx]:
                result += 1
                g_idx += 1
                s_idx += 1
            else:
                s_idx += 1
        return result
# @lc code=end

s = Solution()
s.findContentChildren([10,9,8,7], [5,6,7,8])

