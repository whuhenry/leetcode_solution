#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ''
        while(n > 0):
            result += chr((n - 1) % 26 + ord('A'))
            n =(n - 1) // 26
        return result[::-1]
# @lc code=end

