#
# @lc app=leetcode.cn id=1832 lang=python3
#
# [1832] 判断句子是否为全字母句
#

# @lc code=start
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        charset = set()
        for ch in sentence:
            charset.add(ch)
        if len(charset) != 26:
            return False
        return True
# @lc code=end

