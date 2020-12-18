#
# @lc app=leetcode.cn id=1668 lang=python3
#
# [1668] 最大重复子字符串
#

# @lc code=start
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        max_k = len(sequence) // len(word)
        result = 0
        for i in range(max_k + 1):
            tmp = word * i
            if tmp in sequence:
                result = i
            else:
                break
        return result

# @lc code=end

