#
# @lc app=leetcode.cn id=1624 lang=python3
#
# [1624] 两个相同字符之间的最长子字符串
#

# @lc code=start
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        pre = [-1] * 26
        result = [-1] * 26
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            if pre[idx] == -1:
                pre[idx] = i
            else:
                result[idx] = i - pre[idx] - 1
        return max(result)
# @lc code=end

