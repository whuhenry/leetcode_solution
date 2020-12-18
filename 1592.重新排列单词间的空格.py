#
# @lc app=leetcode.cn id=1592 lang=python3
#
# [1592] 重新排列单词间的空格
#

# @lc code=start
class Solution:
    def reorderSpaces(self, text: str) -> str:
        blank_count = 0
        for ch in text:
            if ch == ' ':
                blank_count += 1
        words = text.split()
        result = ''
        if len(words) == 1:
            result = words[0] + ' ' * blank_count
        else:
            blank_between = blank_count // (len(words) - 1)
            blank_tail = blank_count - blank_between * (len(words) - 1)
            result = ' ' * blank_between
            result = result.join(words) + ' ' * blank_tail
        return result
# @lc code=end

