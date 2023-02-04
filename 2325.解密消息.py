#
# @lc app=leetcode.cn id=2325 lang=python3
#
# [2325] 解密消息
#

# @lc code=start
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        cur_ord = ord('a')
        key_map = {}
        key_map[' '] = ' '
        for ch in key:
            if ch not in key_map:
                key_map[ch] = chr(cur_ord)
                cur_ord += 1
        
        result = ''
        for ch in message:
            result += key_map[ch]
        return result
# @lc code=end

