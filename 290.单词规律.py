#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        pattern_dict = {}
        for i in range(len(pattern)):
            if pattern[i] not in pattern_dict:
                pattern_dict[pattern[i]] = words[i]
            else:
                if pattern_dict[pattern[i]] != words[i]:
                    return False
        
        if len(pattern_dict) != len(set(pattern_dict.values())):
            return False
        
        return True
# @lc code=end

