#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ''
        count = len(s) // (k * 2)
        for i in range(count):
            result += s[i * k * 2: i * k * 2 + k][::-1]
            result += s[i * k * 2 + k : i * k * 2 + k * 2]

        end = min(count * k * 2 + k, len(s))
        result += s[count * k * 2: end][::-1]
        result += s[end: len(s)]
        return result



# @lc code=end