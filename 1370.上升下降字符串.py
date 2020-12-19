#
# @lc app=leetcode.cn id=1370 lang=python3
#
# [1370] 上升下降字符串
#

# @lc code=start
import collections
class Solution:
    def sortString(self, s: str) -> str:
        n = len(s)
        s_count = collections.Counter(s)
        result = ''
        reverse = False
        while n > 0:
            ch_set = list(s_count)
            ch_set.sort(reverse=reverse)
            reverse = not reverse
            result += ''.join(ch_set)
            n -= len(ch_set)
            for ch in ch_set:
                s_count[ch] -= 1
                if s_count[ch] == 0:
                    del(s_count[ch])
        return result

# @lc code=end

s = Solution()
print(s.sortString('spo'))