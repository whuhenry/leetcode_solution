#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#

from typing import List

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        result = []
        for word in words:
            word_low = word.lower()
            idx = None
            valid = True
            for ch in word_low:
                for i, line in enumerate(keyboard):
                    if ch in line:
                        if idx is None:
                            idx = i
                        elif idx != i:
                            valid = False
                        break
                if not valid:
                    break
            if valid:
                result.append(word)
        return result

# @lc code=end