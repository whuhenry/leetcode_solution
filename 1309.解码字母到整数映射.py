#
# @lc app=leetcode.cn id=1309 lang=python3
#
# [1309] 解码字母到整数映射
#

# @lc code=start
class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        idx = len(s) - 1
        while idx >= 0:
            if s[idx] == '#':
                result.append(chr(int(s[idx - 2: idx]) + ord('a') - 1))
                idx -= 3
            else:
                result.append(chr(int(s[idx]) + ord('a') - 1))
                idx -= 1
        return ''.join(result[::-1])
# @lc code=end

