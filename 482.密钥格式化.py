#
# @lc app=leetcode.cn id=482 lang=python3
#
# [482] 密钥格式化
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s = S.replace('-', '').upper()
        first = len(s) % K
        count = len(s) // K
        if first == 0:
            result = ''
        else:
            result = s[0: first] + '-'

        for i in range(count):
            result += s[first + i * K: first + i * K + K] + '-'
        
        return result.strip('-')
        
# @lc code=end

