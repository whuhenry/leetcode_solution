#
# @lc app=leetcode.cn id=925 lang=python3
#
# [925] 长按键入
#

# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        cur_n, cur_t = 0, 0
        while cur_n < len(name) and cur_t < len(typed):
            if name[cur_n] != typed[cur_t]:
                return False
            pre_n, pre_t = cur_n, cur_t
            while cur_n + 1 < len(name) and name[cur_n + 1] == name[cur_n]:
                cur_n += 1
            while cur_t + 1 < len(typed) and typed[cur_t + 1] == typed[cur_t]:
                cur_t += 1
            count_t = cur_t - pre_t
            count_n = cur_n - pre_n
            if count_t < count_n:
                return False
            cur_n += 1
            cur_t += 1
        if cur_n < len(name) or cur_t < len(name):
            return False
        return True
# @lc code=end

s = Solution()
print(s.isLongPressedName('alex', 'aaleex'))