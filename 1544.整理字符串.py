#
# @lc app=leetcode.cn id=1544 lang=python3
#
# [1544] 整理字符串
#

# @lc code=start
class Solution:
    def makeGood(self, s: str) -> str:
        result = ''
        while True:
            flag = True
            idx = 0
            result = ''
            while idx < len(s) - 1:
                tmp = s[idx].islower()
                if s[idx].islower() and s[idx].upper() == s[idx + 1]:
                    idx += 2
                    flag = False
                elif s[idx].isupper() and s[idx].lower() == s[idx + 1]:
                    idx += 2
                    flag = False
                else:
                    result += s[idx]
                    idx += 1
            if idx < len(s):
                result += s[idx]
            if flag:
                break
            s = result
        return result
# @lc code=end

s = Solution()
print(s.makeGood(''))