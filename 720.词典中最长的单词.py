#
# @lc app=leetcode.cn id=720 lang=python3
#
# [720] 词典中最长的单词
#

from typing import List

# @lc code=start
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        words_set = set()
        max_len = 0
        result = ''
        for word in words:
            if len(word) == 1:
                if len(word) > max_len:
                    result = word
                    max_len = len(result)
                words_set.add(word)
            elif word[0: -1] in words_set:
                if len(word) > max_len:
                    result = word
                    max_len = len(result)
                words_set.add(word)
        return result

        
# @lc code=end

