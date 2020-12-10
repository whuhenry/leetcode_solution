#
# @lc app=leetcode.cn id=819 lang=python3
#
# [819] 最常见的单词
#

from typing import List

# @lc code=start
import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.split('[!?\',;.\s]', paragraph.lower())
        words = list(filter(None, words))
        word_count = Counter(words)
        for word, count in word_count.most_common():
            if not word in banned:
                return word
        return ''
        
# @lc code=end

s = Solution()
print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ['hit']))
