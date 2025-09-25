#
# @lc app=leetcode.cn id=1790 lang=python3
#
# [1790] 仅执行一次字符串交换能否使两个字符串相等
#

# @lc code=start
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff_idx = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_idx.append(i)
        if len(diff_idx) == 0:
            return True
        elif len(diff_idx) == 2:
            return s1[diff_idx[0]] == s2[diff_idx[1]] and s1[diff_idx[1]] == s2[diff_idx[0]]
        else:
            return False

# @lc code=end

