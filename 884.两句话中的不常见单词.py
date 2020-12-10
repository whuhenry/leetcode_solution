#
# @lc app=leetcode.cn id=884 lang=python3
#
# [884] 两句话中的不常见单词
#

from typing import List

# @lc code=start
from collections import Counter

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        words = Counter(A.split() + B.split())
        result = []
        for word in words:
            if words[word] == 1:
                result.append(word)
        return result
        
# @lc code=end

