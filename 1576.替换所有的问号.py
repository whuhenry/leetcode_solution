#
# @lc app=leetcode.cn id=1576 lang=python3
#
# [1576] 替换所有的问号
#

# @lc code=start
class Solution:
    def modifyString(self, s: str) -> str:
        if len(s) == 1:
            if s == '?':
                return 'a'
            else:
                return s
        s_list = list(s)
        ch_list = [chr(j + ord('a')) for j in range(26)]
        for i, ch in enumerate(s_list):
            if ch == '?':
                for a in ch_list:
                    if i == 0:
                        if s_list[i + 1] != a:
                            s_list[i] = a
                            break
                    elif i == len(s) - 1:
                        if s_list[i - 1] != a:
                            s_list[i] = a
                            break
                    elif s_list[i - 1] != a and s_list[i + 1] != a:
                        s_list[i] = a
                        break
        return ''.join(s_list)
# @lc code=end

