#
# @lc app=leetcode.cn id=551 lang=python3
#
# [551] 学生出勤记录 I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        A_count = 0
        L_count = 0
        pre = ''
        for ch in s:
            if ch == 'A':
                A_count += 1
                if A_count > 1:
                    return False
            if ch == 'L':
                if pre == 'L':
                    L_count += 1
                    if L_count > 2:
                        return False
                else:
                    L_count = 1
            pre = ch
        return True
                    
# @lc code=end

