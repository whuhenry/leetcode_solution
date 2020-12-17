#
# @lc app=leetcode.cn id=942 lang=python3
#
# [942] 增减字符串匹配
#

from typing import List

# @lc code=start
import collections
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        ch_count = collections.Counter(S)
        D_count = ch_count['D']
        D = D_count
        A = D_count
        result = [D_count]
        for ch in S:
            if ch == 'D':
                D -= 1
                result.append(D)
            elif ch == 'I':
                A += 1
                result.append(A)
        return result
# @lc code=end

