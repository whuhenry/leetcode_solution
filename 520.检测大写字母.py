#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        up_count = 0
        for ch in word:
            if ch.isupper():
                up_count += 1
        if up_count == 0 or up_count == len(word):
            return True
        if up_count == 1 and word[0].isupper():
            return True
        return False
# @lc code=end

