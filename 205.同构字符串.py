#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        chMap = {}
        chUsed = set()
        for i in range(len(s)):
            if s[i] in chMap and t[i] != chMap[s[i]]:
                return False
            elif s[i] not in chMap:
                chMap[s[i]] = t[i]
        
        for k in chMap:
            if chMap[k] in chUsed:
                return False
            else:
                chUsed.add(chMap[k])
        return True
        
# @lc code=end

