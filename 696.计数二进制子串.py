#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pre = None
        pre_count = 0
        cur = s[0]
        cur_count = 1
        result = 0
        for i in range(1, len(s)):
            if s[i] == cur:
                cur_count += 1
            else:
                if pre is not None:
                    result += min(pre_count, cur_count)
                pre = cur
                pre_count = cur_count
                cur = s[i]
                cur_count = 1

        if pre is not None:
            result += min(pre_count, cur_count)
        return result
                
        
# @lc code=end

