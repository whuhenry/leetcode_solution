#
# @lc app=leetcode.cn id=1935 lang=python3
#
# [1935] 可以输入的最大单词数
#

# @lc code=start
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text_list = text.split(' ')
        re = 0
        for word in text_list:
            flag = True
            for ch in brokenLetters:
                if ch in word:
                    flag = False
                    break
            if flag:
                re += 1
        return re
        
# @lc code=end

